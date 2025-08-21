from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from rag_prompt_patch import chat

app = FastAPI()

@app.post("/chat")
async def chat_route(request: Request):
    data = await request.json()
    prompt = data.get("prompt", "")
    response = chat(prompt)
    return JSONResponse(content={"response": response})

# Serve the built React UI
app.mount("/ui", StaticFiles(directory="ui", html=True), name="ui")
