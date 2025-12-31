from flask import Flask
import os
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return f"""
    <h1>Vulnerable App</h1>
    <p>Running as user: {os.getuid()}</p>
    <p>Username: {subprocess.getoutput('whoami')}</p>
    """

@app.route('/exploit')
def exploit():
    # This endpoint demonstrates the danger
    result = subprocess.getoutput('id')
    return f"<pre>{result}</pre>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)