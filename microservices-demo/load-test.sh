


#!/bin/bash

echo "🔥 MICROSERVICES LOAD TEST"
echo "=========================="
echo ""

# Install Apache Bench if not present
if ! command -v ab &> /dev/null; then
    echo "Installing Apache Bench..."
    sudo yum install -y httpd-tools
fi

echo "Testing Product Service (FAST)..."
ab -n 100 -c 10 http://localhost:5001/products > /dev/null 2>&1
echo "✅ Product: 100 requests sent"

echo ""
echo "Testing Cart Service (MEDIUM)..."
ab -n 100 -c 10 http://localhost:5002/cart/user123 > /dev/null 2>&1
echo "✅ Cart: 100 requests sent"

echo ""
echo "Testing Payment Service (SLOW - This will take time!)..."
ab -n 20 -c 5 -p payment-data.json -T application/json http://localhost:5004/payment > /dev/null 2>&1
echo "✅ Payment: 20 requests sent"

echo ""
echo "📊 Check Grafana: http://YOUR_EC2_IP:3000"
echo "📊 Check cAdvisor: http://YOUR_EC2_IP:8080"
echo "📊 Check Prometheus: http://YOUR_EC2_IP:9090"


# chmod +x load-test.sh

# # Create test data for payment
# cat > payment-data.json << 'EOF'
# {"order_id": "ORD-1234", "amount": 1000}
# EOF