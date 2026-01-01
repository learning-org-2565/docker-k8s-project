from flask import Flask, jsonify, request
import time
import random

app = Flask(__name__)

# In-memory "database"
products_db = [
    {"id": 1, "name": "Laptop", "price": 50000, "stock": 10},
    {"id": 2, "name": "Phone", "price": 30000, "stock": 20},
    {"id": 3, "name": "Tablet", "price": 25000, "stock": 15}
]

cart_db = {}
orders_db = {}

# HOME PAGE
@app.route('/')
def home():
    return jsonify({"message": "Monolith E-commerce API"})

# PRODUCT SERVICE (in monolith)
@app.route('/products')
def get_products():
    time.sleep(0.1)  # Simulate DB query
    return jsonify(products_db)

@app.route('/products/<int:product_id>')
def get_product(product_id):
    time.sleep(0.1)
    product = next((p for p in products_db if p['id'] == product_id), None)
    if product:
        return jsonify(product)
    return jsonify({"error": "Product not found"}), 404

# CART SERVICE (in monolith)
@app.route('/cart/<user_id>')
def get_cart(user_id):
    time.sleep(0.1)
    cart = cart_db.get(user_id, {"items": [], "total": 0})
    return jsonify(cart)

@app.route('/cart/<user_id>/add', methods=['POST'])
def add_to_cart(user_id):
    time.sleep(0.1)
    data = request.json
    product_id = data.get('product_id')
    quantity = data.get('quantity', 1)
    
    # Get product
    product = next((p for p in products_db if p['id'] == product_id), None)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    
    # Add to cart
    if user_id not in cart_db:
        cart_db[user_id] = {"items": [], "total": 0}
    
    cart_db[user_id]["items"].append({
        "product_id": product_id,
        "name": product["name"],
        "price": product["price"],
        "quantity": quantity
    })
    cart_db[user_id]["total"] += product["price"] * quantity
    
    return jsonify(cart_db[user_id])

# ORDER SERVICE (in monolith)
@app.route('/orders', methods=['POST'])
def create_order():
    time.sleep(0.2)
    data = request.json
    user_id = data.get('user_id')
    
    cart = cart_db.get(user_id)
    if not cart or not cart["items"]:
        return jsonify({"error": "Cart is empty"}), 400
    
    order_id = f"ORD-{random.randint(1000, 9999)}"
    orders_db[order_id] = {
        "order_id": order_id,
        "user_id": user_id,
        "items": cart["items"],
        "total": cart["total"],
        "status": "processing"
    }
    
    # Clear cart
    cart_db[user_id] = {"items": [], "total": 0}
    
    return jsonify(orders_db[order_id])

@app.route('/orders/<order_id>')
def get_order(order_id):
    time.sleep(0.1)
    order = orders_db.get(order_id)
    if order:
        return jsonify(order)
    return jsonify({"error": "Order not found"}), 404

# PAYMENT SERVICE (in monolith)
@app.route('/payment', methods=['POST'])
def process_payment():
    time.sleep(0.3)
    data = request.json
    order_id = data.get('order_id')
    
    order = orders_db.get(order_id)
    if not order:
        return jsonify({"error": "Order not found"}), 404
    
    # Simulate payment processing
    payment_id = f"PAY-{random.randint(1000, 9999)}"
    order["status"] = "paid"
    order["payment_id"] = payment_id
    
    return jsonify({
        "payment_id": payment_id,
        "order_id": order_id,
        "amount": order["total"],
        "status": "success"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)