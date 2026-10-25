import sqlite3

try:
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

        cursor.execute("INSERT or IGNORE INTO users (username, password) VALUES (?, ?)", ("admin", "admin123"))
        cursor.execute("INSERT or IGNORE INTO users (username, password) VALUES (?, ?)", ("daddy", "supersecure"))
        cursor.execute("INSERT or IGNORE INTO users (username, password) VALUES (?, ?)", ("ella", "weaksauce"))
        conn.commit()

        cursor.execute("SELECT * FROM users")
        while True:
            result = cursor.fetchmany(2)
            if not result:
                break
            else:
                print(result)

except sqlite3.Error as e:
    print(f"An error occurred: {e}")
