from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

DB = "../data/laundromats.db"

@app.route("/")
def home():
    return "OSM Laundromat Dashboard Running"

@app.route("/data")
def data():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute("SELECT name, lat, lon FROM laundromats LIMIT 1000")
    rows = cur.fetchall()

    conn.close()

    return jsonify([
        {"name": r[0], "lat": r[1], "lon": r[2]} for r in rows
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)