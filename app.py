from flask import Flask, request
import sqlite3
import json

def database_initialise():
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

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
       return app.send_static_file("index.html")

@app.route("/registration", methods=["GET"])
def register():
    return app.send_static_file("registration.html")

@app.route("/login", methods=["GET"])
def login():
    return app.send_static_file("login.html")

@app.route("/v1/idk", methods=["POST"])
def idk():
       login = request.form.get('clicked')
       register = request.form.get('clicked')
            

@app.route('/v1/users', methods=["POST"])
def users():
    print(request.form)

    with sqlite3.connect("login.db") as conn:
        cursor = conn.cursor()
        username = request.form.get('username')
        password = request.form.get('password')

        cursor.execute("INSERT or IGNORE INTO users (username, password) VALUES (?,?)", (username, password))

        conn.commit()
        return "OK"
