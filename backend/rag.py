from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

from data.knowledge_base import knowledge_base

documents = []

for item in knowledge_base:

    text = f"""
    Question: {item['question']}
    Answer: {item['answer']}
    """

    documents.append(
        Document(page_content=text)
    )

print("Documents Loaded")

# Split documents

splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)

chunks = splitter.split_documents(documents)

print(f"Created {len(chunks)} chunks")

# Create embeddings

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

print("Embeddings Loaded")

# Create vector database

vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="db"
)

print("Vector Database Created")

# Create retriever

retriever = vectorstore.as_retriever(
    search_kwargs={"k": 2}
)

# Test retrieval

query = "Tell me about refund"

results = retriever.invoke(query)

print("\nRetrieved Results:\n")

for doc in results:
    print(doc.page_content)