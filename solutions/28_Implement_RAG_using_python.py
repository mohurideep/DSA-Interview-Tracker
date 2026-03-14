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
        