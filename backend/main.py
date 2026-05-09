from langchain_groq import ChatGroq

# Initialize model
llm = ChatGroq(
    model="llama-3.3-70b-versatile"
)

print("AI Customer Support Agent Started")
print("Type 'exit' to stop\n")

while True:
    question = input("You: ")

    if question.lower() == "exit":
        print("Chat ended.")
        break

    response = llm.invoke(question)

    print("\nAI:", response.content)
    print()