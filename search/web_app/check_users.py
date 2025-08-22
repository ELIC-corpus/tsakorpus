from web_app.db import get_user
import sqlite3

def list_users():
    conn = sqlite3.connect("web_app/users.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    rows = c.fetchall()
    conn.close()
    for row in rows:
        print(row)

if __name__ == "__main__":
    list_users()
