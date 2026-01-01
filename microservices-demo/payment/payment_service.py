

from flask import Flask, jsonify, request
import time
import random

app = Flask(__name__)

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

@app.route('/payment', methods=['POST'])
def process_payment():
    # VERY SLOW - Simulating external payment gateway!
    # This is like calling Razorpay, Stripe, etc.
    time.sleep(3)  # 3 SECONDS - VERY SLOW! 💀
    
    data = request.json
    payment_id = f"PAY-{random.randint(1000, 9999)}"
    
    return jsonify({
        "payment_id": payment_id,
        "order_id": data.get("order_id"),
        "amount": data.get("amount"),
        "status": "success"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)


