from fastapi import FastAPI, UploadFile, Form, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uuid

app = FastAPI()

# RAM storage
users = {}

MAX_MESSAGES = 5
MAX_IMAGE_SIZE = 50 * 1024  # 50 KB

class SendMessageRequest(BaseModel):
    from_id: str
    to_id: str
    message: str

@app.post("/signup")
async def signup(
    mobile: str = Form(...),
    name: Optional[str] = Form(None),
    image: Optional[UploadFile] = None
):
    # Check for existing mobile number
    for uid, user in users.items():
        if user["mobile"] == mobile:
            return {"status": "exists", "user_id": uid}

    # Check image size if provided
    image_data = None
    if image:
        contents = await image.read()
        if len(contents) > MAX_IMAGE_SIZE:
            raise HTTPException(status_code=400, detail="Image exceeds 50KB limit.")
        image_data = contents  # Store image as bytes

    # Create new user
    user_id = str(uuid.uuid4())
    users[user_id] = {
        "mobile": mobile,
        "name": name or "",
        "image": image_data,
        "messages": []
    }

    return {"status": "created", "user_id": user_id}


@app.post("/send")
def send_message(msg: SendMessageRequest):
    if msg.to_id not in users:
        raise HTTPException(status_code=404, detail="Target user not found")

    target_user = users[msg.to_id]
    
    if len(target_user["messages"]) >= MAX_MESSAGES:
        raise HTTPException(status_code=400, detail="User message queue full (max 5)")

    target_user["messages"].append({
        "from": msg.from_id,
        "text": msg.message
    })

    return {"status": "sent"}


@app.get("/receive/{user_id}")
def receive_messages(user_id: str):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")

    messages = users[user_id]["messages"]
    users[user_id]["messages"] = []  # Clear after retrieval
    return {"messages": messages}


@app.get("/users")
def list_users():
    return {
        uid: {
            "mobile": user["mobile"],
            "name": user["name"]
        } for uid, user in users.items()
    }
