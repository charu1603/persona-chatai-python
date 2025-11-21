from fastapi import FastAPI
from pydantic import BaseModel
import json
from personas.persona1 import persona1_reply
from personas.persona2 import persona2_reply
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

FAV_FILE = "db/favorites.json"

class ChatRequest(BaseModel):
    persona: str
    message: str
    is_favorite: bool = False
@app.get("/")
def root():
    return {"status": 200, "message": "Backend running OK on port 5000"}

@app.post("/chat")
def chat(req: ChatRequest):
    if req.persona == "persona1":
        reply = persona1_reply(req.message)
    else:
        reply = persona2_reply(req.message)

    if req.is_favorite:
        save_favorite(req.message, reply)

    return {"reply": reply}

@app.get("/favorites")
def get_favorites():
    with open(FAV_FILE, "r") as f:
        return json.load(f)

def save_favorite(user, bot):
    with open(FAV_FILE, "r") as f:
        data = json.load(f)

    data.append({"user": user, "bot": bot})

    with open(FAV_FILE, "w") as f:
        json.dump(data, f, indent=2)
