from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host=os.environ['DB_HOST'],
        database=os.environ['DB_NAME'],
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASSWORD']
    )
    return conn

@app.route('/')
def home():
    return jsonify({"message": "Backend API is running!"})

@app.route('/users')
def get_users():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT id, name FROM users;')
    users = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify([{"id": u[0], "name": u[1]} for u in users])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)