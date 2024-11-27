from flask import Flask, jsonify, request
import psycopg2
from psycopg2.extras import Json
from flask_cors import CORS
import os
import json

app = Flask(__name__)
CORS(app)

# connect to db
conn = psycopg2.connect(
    host=os.environ["DB_HOST"],
    port=os.environ["DB_PORT"],
    dbname=os.environ["DB_NAME"],
    user=os.environ["DB_USER"],
    password=os.environ["DB_PASSWORD"]
)

@app.route('/api/locations', methods=['GET'])
def get_locations():
    cur = conn.cursor()
    cur.execute("SELECT id, name, description, ST_AsGeoJSON(geom) FROM locations;")
    locations = [{"id": row[0], "name": row[1], "description": row[2], "geom": row[3]} for row in cur.fetchall()]
    cur.close()
    return jsonify(locations)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
