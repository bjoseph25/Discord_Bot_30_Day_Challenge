import sqlite3
import os

def connect(db_path: str):
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    return sqlite3.connect(db_path)

def init_db(conn):
    conn.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        discord_id TEXT UNIQUE,
        points INTEGER DEFAULT 0
    )
    """)
    conn.commit()
