import requests
import sqlite3
import os

OVERPASS_URL = os.getenv("OVERPASS_URL", "https://overpass-api.de/api/interpreter")
DB_PATH = "data/laundromats.db"

QUERY = """
[out:json][timeout:180];
area["ISO3166-1"="US"]->.usa;
(
  node["amenity"="laundry"](area.usa);
  way["amenity"="laundry"](area.usa);
  relation["amenity"="laundry"](area.usa);
);
out center;
"""

def fetch():
    r = requests.post(OVERPASS_URL, data=QUERY)
    return r.json()

def save(data):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    inserted = 0

    for el in data.get("elements", []):
        tags = el.get("tags", {})

        name = tags.get("name", "Unknown")
        lat = el.get("lat") or el.get("center", {}).get("lat")
        lon = el.get("lon") or el.get("center", {}).get("lon")
        osm_id = f"{el.get('type')}/{el.get('id')}"

        if not lat or not lon:
            continue

        cur.execute("""
            INSERT OR IGNORE INTO laundromats (name, lat, lon, osm_id)
            VALUES (?, ?, ?, ?)
        """, (name, lat, lon, osm_id))

        inserted += 1

    conn.commit()
    conn.close()

    print(f"Inserted: {inserted}")

if __name__ == "__main__":
    data = fetch()
    save(data)