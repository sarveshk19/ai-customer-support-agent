import { useState } from "react"

function App() {

  const [message, setMessage] = useState("")
  const [chat, setChat] = useState([])

  const sendMessage = async () => {

    if (!message) return

    const userMessage = {
      role: "user",
      text: message
    }

    const updatedChat = [
      ...chat,
      userMessage
    ]

    setChat(updatedChat)

    setMessage("")

    try {

      const response = await fetch(
        "http://127.0.0.1:8000/chat",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            message: message
          })
        }
      )

      const data = await response.json()

      setChat([
        ...updatedChat,
        {
          role: "ai",
          text: data.response
        }
      ])

    } catch (error) {

      console.log(error)

    }
  }

  return (
    <div style={styles.container}>

      <h1>AI Customer Support Agent</h1>

      <div style={styles.chatBox}>

        {chat.map((msg, index) => (

          <div
            key={index}
            style={
              msg.role === "user"
                ? styles.userMessage
                : styles.aiMessage
            }
          >
            {msg.text}
          </div>

        ))}

      </div>

      <div style={styles.inputArea}>

        <input
          type="text"
          placeholder="Ask something..."
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          style={styles.input}
        />

        <button
          onClick={sendMessage}
          style={styles.button}
        >
          Send
        </button>

      </div>

    </div>
  )
}

const styles = {

  container: {
    width: "100%",
    maxWidth: "800px",
    margin: "auto",
    padding: "20px",
    fontFamily: "Arial"
  },

  chatBox: {
    height: "500px",
    border: "1px solid #ccc",
    padding: "10px",
    overflowY: "auto",
    marginBottom: "20px"
  },

  userMessage: {
    background: "#007bff",
    color: "white",
    padding: "10px",
    borderRadius: "10px",
    marginBottom: "10px",
    textAlign: "right"
  },

  aiMessage: {
    background: "#f1f1f1",
    padding: "10px",
    borderRadius: "10px",
    marginBottom: "10px"
  },

  inputArea: {
    display: "flex",
    gap: "10px"
  },

  input: {
    flex: 1,
    padding: "10px"
  },

  button: {
    padding: "10px 20px",
    cursor: "pointer"
  }
}

export default App