import os, sys
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

sys.path.append(os.path.dirname(__file__))
from rag_prompt_patch import improve_prompt_context

app = FastAPI(title="Franklin AI Middleware")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

try:
    ui_dir = "/app/ui"
    if os.path.isdir(ui_dir):
        from fastapi.staticfiles import StaticFiles
        app.mount("/ui", StaticFiles(directory=ui_dir, html=True), name="ui")
except Exception:
    pass

class ChatIn(BaseModel):
    prompt: str

@app.get("/")
def root():
    return {"status": "ok"}

@app.get("/health")
def health():
    return {"ok": True}

@app.post("/chat")
def chat(inp: ChatIn):
    try:
        result = improve_prompt_context(inp.prompt)
        if isinstance(result, (str, list, dict, int, float, bool)) or result is None:
            return {"response": result}
        return {"response": repr(result)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))