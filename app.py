from flask import Flask, request
import sqlite3
import json

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return """
    <html>
    <head>
    <title>Login</title>
    </head>
    <body>

    <h1>Login</h1>

    <form>
    <label for="fname">FUsername:</label><br>
    <input type="text" id="fname"><br>
    <label for="lname">Password:</label><br>
    <input type="text" id="lname">
    </form>

    </body>
    </html>
"""

@app.route('/users',methods=["POST","GET"])
def users():
    if request.method == 'POST':
        print(request.json)
        with sqlite3.connect("login.db") as conn:
            cursor = conn.cursor()
            cursor.execute(
                """CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL
                )"""
            )
            conn.commit()

            cursor.execute("INSERT or IGNORE INTO users (username, password) VALUES (?, ?)", (request.json["username"], request.json["password"]))
            conn.commit()
        return "OK"
    else:
        with sqlite3.connect("login.db") as conn:
            cursor = conn.cursor()
            cursor.execute(
                """CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL
                )"""
            )
            conn.commit()

            cursor.execute("SELECT * FROM users")
            result = cursor.fetchall()
            return json.dumps(result)




