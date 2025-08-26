from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse

from rag_prompt_patch import improve_prompt_context

app = FastAPI()

# Serve built Web UI at /ui
app.mount("/ui", StaticFiles(directory="app/static/ui", html=True), name="ui")

# Serve favicon at /favicon.ico
@app.get("/favicon.ico", include_in_schema=False)
@app.head("/favicon.ico", include_in_schema=False)
def favicon():
    return FileResponse("app/static/favicon.ico")

# POST route for Franklin chat
@app.post("/chat")
async def chat(request: Request):
    body = await request.json()
    prompt = body.get("prompt", "")
    response = improve_prompt_context(prompt)
    return JSONResponse(content={"response": response})

# Root check
@app.get("/")
def root():
    return {"message": "Franklin Core is live."}
