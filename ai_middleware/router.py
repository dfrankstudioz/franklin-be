from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class ChatRequest(BaseModel):
    prompt: str

@router.post("/chat")
async def chat_handler(request: ChatRequest):
    return {"response": f"pong: {request.prompt}"}
