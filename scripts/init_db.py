import sqlite3
import os

os.makedirs("data", exist_ok=True)

conn = sqlite3.connect("data/laundromats.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS laundromats (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    lat REAL,
    lon REAL,
    osm_id TEXT UNIQUE
)
""")

conn.commit()
conn.close()

print("Database initialized")