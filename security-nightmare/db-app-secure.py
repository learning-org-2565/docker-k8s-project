from flask import Flask
import os

app = Flask(__name__)

# PROPER WAY: Read secrets from files
def read_secret(secret_name):
    """Read secret from file (Docker secrets pattern)"""
    secret_path = f'/run/secrets/{secret_name}'
    try:
        with open(secret_path, 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        return f"SECRET_{secret_name}_NOT_FOUND"

# Read secrets from files (NOT environment variables!)
DB_HOST = os.getenv('DB_HOST', 'localhost')  # Non-sensitive config = OK in env
DB_USER = os.getenv('DB_USER', 'admin')      # Non-sensitive config = OK in env
DB_PASSWORD = read_secret('db_password')     # ✅ SECURE!
API_KEY = read_secret('api_key')             # ✅ SECURE!

@app.route('/')
def home():
    return f"""
    <h1>Database Connection Info (SECURE)</h1>
    <p>Host: {DB_HOST}</p>
    <p>User: {DB_USER}</p>
    <p>Password: {'*' * len(DB_PASSWORD)}</p>
    """

@app.route('/health')
def health:
    return "OK"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)