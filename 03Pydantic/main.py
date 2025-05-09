from fastapi import FastAPI, HTTPException
from pydantic import BaseModel , Field
from datetime import datetime, UTC
from uuid import uuid4

app = FastAPI(
    title="DACA Chatbot API",
    description="A FastAPI-based API for a chatbot in the DACA tutorial series",
    version="0.1.0",
)
class Metadata(BaseModel):
    timestamp:datetime=Field(default_factory=lambda:datetime.now(tz=UTC))
    session_id:str=Field(default_factory=lambda:str(uuid4()))

class User_message(BaseModel):
    user_id:str
    text:str 
    metadata:Metadata
    tags:list[str]|None=None     

class Chatbot_Response(BaseModel):
    user_id:str
    reply:str
    metadata:Metadata

@app.get("/")
async def root():
    return {"message": "Welcome to the DACA Chatbot API! Access /docs for the API documentation."}

@app.get("/users/{user_id}")
async def get_user(user_id: str, role: str | None = None) :
    user_info={"user_id":user_id, "role": role if role else "guest" }
    return user_info   

@app.post("/chat/", response_model=Chatbot_Response)
async def chat(message:User_message):
    if not message.text.strip():
        raise HTTPException(
            status_code=400, detail="Message text cannot be empty")
    reply_text=f"Hello, {message.user_id}! You said: '{message.text}'. How can I assist you today?"
    return Chatbot_Response(
        user_id=message.user_id,
        reply=reply_text,
        metadata=Metadata()
    )