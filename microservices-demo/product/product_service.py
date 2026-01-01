
from flask import Flask, jsonify
import time

app = Flask(__name__)

# Simulated database
products = [
    {"id": 1, "name": "Laptop", "price": 50000, "stock": 10},
    {"id": 2, "name": "Phone", "price": 30000, "stock": 20},
    {"id": 3, "name": "Tablet", "price": 25000, "stock": 15}
]

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

@app.route('/products')
def get_products():
    # Fast database read (simulated)
    time.sleep(0.01)  # 10ms - FAST!
    return jsonify(products)

@app.route('/products/<int:product_id>')
def get_product(product_id):
    time.sleep(0.01)  # 10ms - FAST!
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        return jsonify(product)
    return jsonify({"error": "Not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
