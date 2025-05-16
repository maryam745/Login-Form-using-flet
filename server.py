import sqlite3
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Database Initialization
def init_db():
    with sqlite3.connect("users.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                password TEXT NOT NULL
            )
        """)
        conn.commit()

init_db()  # Initialize DB on startup


class User(BaseModel):
    id: int
    name: str
    password: str


@app.post("/register/")
def register_user(user: User):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # Check if user already exists
    cursor.execute("SELECT * FROM users WHERE id=?", (user.id,))
    if cursor.fetchone():
        conn.close()
        raise HTTPException(status_code=400, detail="User already exists!")

    cursor.execute("INSERT INTO users (id, name, password) VALUES (?, ?, ?)", (user.id, user.name, user.password))
    conn.commit()
    conn.close()
    
    return {"message": "User registered successfully!"}


class LoginRequest(BaseModel):
    id: int
    password: str

@app.post("/login/")
def login_user(user: LoginRequest):
    print("called")
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("SELECT password FROM users WHERE id=?", (user.id,))
    user_data = cursor.fetchone()
    conn.close()
    
    if not user_data or user.password != user_data[0]:
            raise HTTPException(status_code=401, detail="Invalid ID or password!")

    return {"message": "Login successful!", "user_id": user.id}