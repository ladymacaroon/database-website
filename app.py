from flask import Flask, jsonify, request
import sqlite3
import json
import hashlib

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
def login():
    return app.send_static_file("login.html")

@app.route("/registration", methods=["GET"])
def register():
    return app.send_static_file("registration.html")

@app.route('/v1/users', methods=["POST"])
def users():
    username = request.form.get('username')
    password = request.form.get('password')

    if not username or not password:
        return jsonify(success=False, message="Enter both a username and password."), 400

    with sqlite3.connect("login.db") as conn:
        cursor = conn.cursor()
        password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
        case_corrected_username = username.lower()

        cursor.execute("INSERT or IGNORE INTO users (username, password) VALUES (?,?)", (case_corrected_username, password_hash))

        if cursor.rowcount == 0:
            return jsonify(success=False, message="That username is already registered."), 409

        conn.commit()
        return jsonify(success=True, message="Registration successful.")
