from langchain_groq import ChatGroq
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

# Load embeddings

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load vector database

vectorstore = Chroma(
    persist_directory="db",
    embedding_function=embeddings
)

# Create retriever

retriever = vectorstore.as_retriever(
    search_kwargs={"k": 2}
)

# Initialize LLM

llm = ChatGroq(
    model="llama-3.3-70b-versatile"
)

print("AI Customer Support Agent Started")
print("Type 'exit' to stop\n")

while True:

    question = input("You: ")

    if question.lower() == "exit":
        print("Chat ended")
        break

    # Retrieve context

    docs = retriever.invoke(question)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    # Prompt

    prompt = f"""
You are an AI customer support assistant.

Answer ONLY from provided context.

Context:
{context}

Question:
{question}
"""

    # Generate response

    response = llm.invoke(prompt)

    print("\nAI:", response.content)
    print()