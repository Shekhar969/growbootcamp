import json
import secrets
from typing import Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

cloudTechMembers = FastAPI()

MEMBERS_FILE = "members.json"
TOKENS_FILE = "tokens.json"

def load(file):
    try:
        with open(file) as f:
            return json.load(f)
    except:
        return []


Members = load(MEMBERS_FILE)
Tokens= load(TOKENS_FILE)

#defining auth members then giving them a auth token that can be used in the header 
class authmember(BaseModel):
    username: str
    password: str

class member(BaseModel):
    id: int
    memberName: str
    role: str

class memberUpdate(BaseModel):
    id: Optional[int] = None
    memberName: Optional[str] = None
    role: Optional[str] = None

@cloudTechMembers.post("/Members")
def add_new_member(m: member):
    Members.append(m.model_dump())
    with open(MEMBERS_FILE, "w") as f: json.dump(Members, f)
    return {"message": "Member added successfully", "member": m}

#auth section
@cloudTechMembers.post("/auth")
def auth_user(user: authmember):
    token = secrets.token_hex(32)

    Tokens.append({
        "name": user.username,
        "password": user.password,
        "token": token
    })

    save_tokens()

    return {
        "access_token": token
    }

def save_tokens():
    with open(TOKENS_FILE, "w") as f:
        json.dump(Tokens, f)


#Member section
@cloudTechMembers.put("/Members/{member_id}")
def update_member(member_id: int, m: member):
    if member_id < len(Members):
        Members[member_id] = m.model_dump()
        with open(MEMBERS_FILE, "w") as f: json.dump(Members, f)
        return m
    raise HTTPException(status_code=404, detail=f"Member {member_id} is failed to chance detail")

@cloudTechMembers.patch("/Members/{member_id}")
def patch_member(member_id: int, m: memberUpdate):
    if member_id < len(Members):
        update_data = m.model_dump(exclude_unset=True)
        Members[member_id].update(update_data)
        with open(MEMBERS_FILE, "w") as f: json.dump(Members, f)
        return Members[member_id]
    raise HTTPException(status_code=404, detail=f"Member {member_id} is failed to edit")

@cloudTechMembers.delete("/Members/{member_id}")
def delete_member(member_id: int):
    if member_id < len(Members):
        removed = Members.pop(member_id)
        with open(MEMBERS_FILE, "w") as f: json.dump(Members, f)
        return {"message": "Deleted successfully", "member": removed}
    raise HTTPException(status_code=404, detail=f"Member {member_id} is failed to dowload")

@cloudTechMembers.get("/Members")
def get_all(limit: int = 10):
    return Members[:limit]

@cloudTechMembers.get("/Members/{member_id}")
def get_member(member_id: int):
    if member_id < len(Members): return Members[member_id]
    raise HTTPException(status_code=404, detail=f"Member {member_id} is not found")