import os
import sqlite3

DB_PATH = os.path.join(os.path.dirname(__file__), "users.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS users (
        email TEXT PRIMARY KEY,
        password TEXT,
        institution TEXT,
        department TEXT,
        designation TEXT
    )
    """)
    conn.commit()
    conn.close()

def add_user(email, password, institution, department, designation):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    try:
        c.execute("""
        INSERT INTO users (email, password, institution, department, designation)
        VALUES (?, ?, ?, ?, ?)
        """, (email, password, institution, department, designation))
        conn.commit()
    except sqlite3.IntegrityError:
        # email already exists
        conn.close()
        return False
    conn.close()
    return True

def get_user(email):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row   # <-- makes rows behave like dicts
    c = conn.cursor()
    c.execute("""
        SELECT email, password, institution, department, designation
        FROM users WHERE email = ?
    """, (email,))
    row = c.fetchone()
    conn.close()
    return dict(row) if row else None
