embed = None
cosine_similarity = None
llm = None

# simplest RAG Function
def rag(query, document):
    query_vec = embed(query)

    scores = []
    for doc in document:
        score = cosine_similarity(query_vec, embed(doc))
        scores.append((doc , score))
    
    scores.sort(key=lambda x : x[1], reverse=True)
    context = "\n".join([doc for doc,_ in scores[:3]])

    return llm(context + "\n question: "+ query)

# bit descriptive version without using langchain
#imports
# from sentence_transformer import SentenceTransformer
# import numpy as np
# from sklearn.metrics.pairwise import cosine_similarity
# from llmmodel_provider import llmmodel

SentenceTransformer = None
np = None
cosine_similarity = None
llmmodel = None
# step 1 embedding model
embedding_model = SentenceTransformer("All_miniLM_L6_v2")

# document prepare
document = [
    "RAG stands for Retrieval Augmented Generation.",
    "It combines document retrieval with large language models.",
    "Vector databases store embeddings for semantic search.",
    "Embeddings convert text into numerical vectors."
]

# precompute embedding for documents
doc_embeddings = embedding_model.encode(document)

# retreive relavant documents
def retreive(query : str, top_k:int = 3):
    query_embeding = embedding_model.encode(query)

    #compute similarity
    similarity_score = cosine_similarity(query_embeding,doc_embeddings)[0]

    # get indices of top k docs
    top_indices = np.argsort(similarity_score)[::-1][:top_k]

    # fetch the doc
    retreive_docs = [document[i] for i in top_indices]

    return retreive_docs

# build context
def build_context(retreive_docs):
    context_block = []

    for i , doc in enumerate(retreive_docs):
        context_block.append(f"[Doc {i+1}] {doc}")

    context = "\n".join(context_block)

    return context

# LLM Generation and built result
client = llmmodel()
def generate_answer(query: str, context: str):

    prompt = f"""
You are an assistant that answer questions using only the provided context.

context: {context}

question: {query}
If the anwer is not present then answer with "Not Found".
"""
    response = client.chat.completion.create(
        model = "llmmodel",
        message = [
            {"role": "system", "content": "assistant_prompt"},
            {"role": "user", "content": prompt}],
        temperature = 0        
    )
    return response.choices[0].message.content

#full rag pipeline
def rag_pipeline(query: str):
    retreive_docs = retreive(query)
    context = build_context(retreive_docs)
    answer = generate_answer(query, context)
    
    return {
        "answer": answer,
        "retrieved_docs": retreive_docs,
        "context": context,
        "query": query
    }

#example Run
if __name__ == "__main__":
    query = "What is RAG?"
    result = rag_pipeline(query)
    print(result)


#Function for top -k retreival
def top_k(query_embedding, document_embedding, k=3):
    scores = []
    for i,emb in enumerate(document_embedding):
        score = cosine_similarity(query_embedding, emb)
        scores.append((i, score))
    scores.sort(key=lambda x: x[1], reverse=True)
    top_indices = [i for i, _ in scores[:k]]
    return top_indices

# Implement Character based chunking
def chunk_text(document, chunk_size=200, overlap=50):
    chunks = []
    start = 0

    while start < len(document):
        end = min(start + chunk_size, len(document))
        chunks.append(document[start:end])
        start = end - overlap  # move back by overlap for next chunk

    return chunks