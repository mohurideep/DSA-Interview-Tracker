# import PyPDF2
# from langchain.textsplitter import CharacterTextSplitter
# from langchain.embeddings.openai import OpenAIEmbeddings
# from langchain.vectorstore import FAISS
# from langchain.chat_models import ChatOpenAI
# For Ignoring errors
PyPDF2 = None
CharacterTextSplitter = None
OpenAIEmbeddings = None
FAISS = None
ChatOpenAI = None

# read pdf
reader = PyPDF2.PdfReader("Document.pdf")
text = ""

for page in reader.pages:
    text += page.extract_text()

# Chunking
splitter = CharacterTextSplitter(
    chunk_size = 500,
    chunk_overlap = 50
)
chunks =  splitter.split_text(text)

#embeddings + vector Store
embeddings = OpenAIEmbeddings()
vector_db = FAISS.from_texts(chunks, embeddings)

# Query
query = "What is the main topic of the document?"

# Retrieval
docs = vector_db.similarity_search(query, k=4)

context = "\n".join([doc.page_content for doc in docs])

# LLM
llm = ChatOpenAI()

prompt = f"""
Use the following context to answer the question.

Context:
{context}

Question:
{query}

If the answer is not in the context, say "Not found".
"""

response = llm.predict(prompt)

print(response)