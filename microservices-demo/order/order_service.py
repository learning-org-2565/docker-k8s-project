
from flask import Flask, jsonify, request
import time
import random

app = Flask(__name__)

orders = {}

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

@app.route('/orders', methods=['POST'])
def create_order():
    # SLOW - Complex business logic + database writes
    time.sleep(0.2)  # 200ms - SLOW!
    
    # Simulate business logic
    data = request.json
    order_id = f"ORD-{random.randint(1000, 9999)}"
    
    # Simulate database write
    orders[order_id] = {
        "order_id": order_id,
        "user_id": data.get("user_id"),
        "total": data.get("total"),
        "status": "processing"
    }
    
    return jsonify(orders[order_id])

@app.route('/orders/<order_id>')
def get_order(order_id):
    time.sleep(0.1)  # 100ms - MEDIUM
    order = orders.get(order_id)
    if order:
        return jsonify(order)
    return jsonify({"error": "Not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
