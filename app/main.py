from fastapi import FastAPI, HTTPException
from app.schema.auth import UserRegister, UserLogin

app = FastAPI()

fake_users_db = {}


@app.post("/register")
def register(user: UserRegister):
    if user.email in fake_users_db:
        raise HTTPException(status_code=400, detail="User already exists")

    fake_users_db[user.email] = user.password
    return {"message": "User registered successfully"}


@app.post("/login")
def login(user: UserLogin):
    if user.email not in fake_users_db:
        raise HTTPException(status_code=404, detail="User not found")

    if fake_users_db[user.email] != user.password:
        raise HTTPException(status_code=401, detail="Invalid password")

    return {"message": "Login successful"}
