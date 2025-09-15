# app/db.py
import os
import psycopg2
import psycopg2.extras
import psycopg2.errors

DATABASE_URL = os.getenv("DATABASE_URL")
if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

def get_conn():
    if not DATABASE_URL:
        raise RuntimeError("DATABASE_URL not set")
    return psycopg2.connect(
        DATABASE_URL,
        cursor_factory=psycopg2.extras.RealDictCursor,
        sslmode="require",
    )

def init_db():
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            email TEXT PRIMARY KEY,
            password TEXT NOT NULL,
            institution TEXT,
            department TEXT
        )
        """)
        conn.commit()

# def add_user(email, password, institution, department):
#     with get_conn() as conn, conn.cursor() as cur:
#         try:
#             cur.execute("""
#                 INSERT INTO users (email, password, institution, department)
#                 VALUES (%s, %s, %s, %s)
#             """, (email, password, institution, department))
#             conn.commit()
#             return True
#         except psycopg2.errors.UniqueViolation:
#             conn.rollback()
#             return False

def add_user(email, password, institution, department, *rest):
    with get_conn() as conn, conn.cursor() as cur:
        try:
            cur.execute("""
                INSERT INTO users (email, password, institution, department)
                VALUES (%s, %s, %s, %s)
            """, (email, password, institution, department))
            conn.commit()
            return True
        except psycopg2.errors.UniqueViolation:
            conn.rollback()
            return False

def get_user(email):
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute("""
            SELECT email, password, institution, department
            FROM users
            WHERE email = %s
        """, (email,))
        row = cur.fetchone()
        return dict(row) if row else None
