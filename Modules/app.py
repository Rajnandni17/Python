from flask import Flask, request
import sqlite3

app = Flask(__name__)


# Create database and users table
conn = sqlite3.connect("users.db")

conn.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL,
    password TEXT NOT NULL
)
""")

conn.commit()
conn.close()


# Signup API
@app.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()

    email = data["email"]
    password = data["password"]

    conn = sqlite3.connect("users.db")

    conn.execute(
        "INSERT INTO users (email, password) VALUES (?, ?)",
        (email, password)
    )

    conn.commit()
    conn.close()

    return {
        "message": "Signup successful",
        "email": email
    }, 201


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    email = data["email"]
    password = data["password"]

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE email = ? AND password = ?",
        (email, password)
    )

    user = cursor.fetchone()

    conn.close()

    if user:
        return {
            "message": "Login successful",
            "email": email
        }, 200

    return {
        "message": "Invalid email or password"
    }, 401


if __name__ == "__main__":
    app.run(debug=True)