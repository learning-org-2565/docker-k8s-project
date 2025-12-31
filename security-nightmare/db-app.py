from flask import Flask
import os

app = Flask(__name__)

# COMMON MISTAKE: Reading secrets from environment variables
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_USER = os.getenv('DB_USER', 'admin')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'default_password')  # ❌ DANGEROUS!
API_KEY = os.getenv('API_KEY', 'sk-1234567890')  # ❌ DANGEROUS!

@app.route('/')
def home():
    return f"""
    <h1>Database Connection Info</h1>
    <p>Host: {DB_HOST}</p>
    <p>User: {DB_USER}</p>
    <p>Password: {'*' * len(DB_PASSWORD)}</p>
    """

@app.route('/health')
def health():
    return "OK"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)