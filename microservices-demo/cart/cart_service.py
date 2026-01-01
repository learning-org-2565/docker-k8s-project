
from flask import Flask, jsonify, request
import time

app = Flask(__name__)

# In-memory cart storage
carts = {}

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

@app.route('/cart/<user_id>')
def get_cart(user_id):
    # Medium - in-memory lookup with some logic
    time.sleep(0.05)  # 50ms - MEDIUM
    cart = carts.get(user_id, {"items": [], "total": 0})
    return jsonify(cart)

@app.route('/cart/<user_id>/add', methods=['POST'])
def add_to_cart(user_id):
    time.sleep(0.08)  # 80ms - MEDIUM (writes are slower)
    data = request.json
    
    if user_id not in carts:
        carts[user_id] = {"items": [], "total": 0}
    
    carts[user_id]["items"].append(data)
    carts[user_id]["total"] += data.get("price", 0) * data.get("quantity", 1)
    
    return jsonify(carts[user_id])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
