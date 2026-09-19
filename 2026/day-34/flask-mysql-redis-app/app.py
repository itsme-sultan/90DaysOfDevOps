import os
import redis
import mysql.connector
from flask import Flask, render_template

app = Flask(__name__)

r = redis.Redis(host=os.getenv("REDIS_HOST", "redis"), port=6379, decode_responses=True)

def get_db():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "db"),
        user=os.getenv("DB_USER", "appuser"),
        password=os.getenv("DB_PASSWORD", "apppassword"),
        database=os.getenv("DB_NAME", "appdb"),
    )

@app.route("/")
def index():
    hits = r.incr("hits")

    db = get_db()
    cur = db.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS visits (id INT AUTO_INCREMENT PRIMARY KEY)")
    cur.execute("INSERT INTO visits () VALUES ()")
    db.commit()
    cur.execute("SELECT COUNT(*) FROM visits")
    total_visits = cur.fetchone()[0]
    cur.close()
    db.close()

    return render_template("index.html", hits=hits, total_visits=total_visits)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
