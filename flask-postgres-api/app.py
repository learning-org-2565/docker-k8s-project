
from flask import Flask, jsonify
import psycopg2
import os
import time

app = Flask(__name__)

def get_db_connection():
    """Connect to PostgreSQL database"""
    conn = psycopg2.connect(
        host=os.getenv('DB_HOST', 'database'),
        database=os.getenv('DB_NAME', 'testdb'),
        user=os.getenv('DB_USER', 'postgres'),
        password=os.getenv('DB_PASSWORD', 'postgres'),
        port=os.getenv('DB_PORT', '5432')
    )
    return conn

@app.route('/')
def home():
    return jsonify({"message": "Flask API is running!"})

@app.route('/health')
def health():
    """Health check endpoint"""
    try:
        conn = get_db_connection()
        conn.close()
        return jsonify({"status": "healthy", "database": "connected"}), 200
    except Exception as e:
        return jsonify({"status": "unhealthy", "error": str(e)}), 500

@app.route('/users')
def users():
    """Get all users from database"""
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM users;')
        users = cur.fetchall()
        cur.close()
        conn.close()
        return jsonify({"users": users})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    time.sleep(5)
    app.run(host='0.0.0.0', port=5000)
