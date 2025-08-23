import { useState } from "react";

function App() {
  const [prompt, setPrompt] = useState("");
  const [response, setResponse] = useState("");

  const sendPrompt = async () => {
    if (!prompt.trim()) return;
    setResponse("Loading...");

    try {
      const res = await fetch("/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ prompt })
      });

      const data = await res.json();
      setResponse(data.response || "No response");
    } catch (err) {
      console.error(err);
      setResponse("Error connecting to backend.");
    }
  };

  return (
    <div style={{ padding: "2rem", fontFamily: "sans-serif" }}>
      <h1>Franklin Web UI</h1>
      <textarea
        rows="4"
        cols="60"
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
        placeholder="Enter your prompt here"
      />
      <br />
      <button onClick={sendPrompt} style={{ marginTop: "1rem" }}>
        Send
      </button>
      <h2>Response:</h2>
      <pre>{typeof response === 'string' ? response : JSON.stringify(response, null, 2)}</pre>
    </div>
  );
}

export default App;
