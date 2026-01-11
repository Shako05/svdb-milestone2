from fastapi import FastAPI
from pymongo import MongoClient
import socket
import os

app = FastAPI()
client = MongoClient("mongodb://mongo-service:27017/")
db = client["svdb"]
names = db["names"]

@app.get("/user")
def get_user():
    # Eerste document uit users/names collectie (ongeacht _id)
    doc = names.find_one({}, {"name": 1})  # Project alleen name veld
    return {"name": doc["name"] if doc else "Demo User"}

@app.get("/containerid")
def get_containerid():
    return {"container_id": socket.gethostname()}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/setname/{newname}")
def set_name(newname: str):
    names.update_one({"_id": "svdb"}, {"$set": {"name": newname}}, upsert=True)
    return {"status": "updated"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
