import json
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

cloudTechMembers, FILE = FastAPI(), "members.json"

def load():
    try:
        with open(FILE) as f: return json.load(f)
    except: return []

Members = load()

class member(BaseModel):
    id: int
    memberName: str
    role: str

@cloudTechMembers.post("/Members")
def add_new_member(m: member):
    Members.append(m.model_dump())
    with open(FILE, "w") as f: json.dump(Members, f)
    return m

@cloudTechMembers.put("/Members/{member_id}")
def update_member(member_id: int, m: member):
    if member_id < len(Members):
        Members[member_id] = m.model_dump()
        with open(FILE, "w") as f: json.dump(Members, f)
        return m
    raise HTTPException(404, detail="Member not found")

@cloudTechMembers.get("/Members")
def get_all_members(limit: int = 10):
    return Members[:limit]

@cloudTechMembers.get("/Members/{member_id}")
def get_member_byId(member_id: int):
    if member_id < len(Members): 
        return Members[member_id]
    raise HTTPException(status_code=404, detail=f"Member {member_id} not found")