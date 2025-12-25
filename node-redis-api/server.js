
const express = require('express');
const redis = require('redis');

const app = express();
const PORT = 3000;

// Redis client
let redisClient;
let server;
let isShuttingDown = false;

// Connect to Redis
async function connectRedis() {
    redisClient = redis.createClient({
        socket: {
            host: process.env.REDIS_HOST || 'redis',
            port: process.env.REDIS_PORT || 6379
        }
    });
    
    await redisClient.connect();
    console.log('✅ Connected to Redis');
}

// Middleware to reject requests during shutdown
app.use((req, res, next) => {
    if (isShuttingDown) {
        res.status(503).json({ error: 'Server is shutting down' });
    } else {
        next();
    }
});

// Routes
app.get('/', (req, res) => {
    res.json({ message: 'Node.js API with Redis is running!' });
});

app.get('/health', async (req, res) => {
    try {
        await redisClient.ping();
        res.json({ status: 'healthy', redis: 'connected' });
    } catch (err) {
        res.status(500).json({ status: 'unhealthy', error: err.message });
    }
});

// Slow endpoint to test graceful shutdown
app.get('/slow', async (req, res) => {
    console.log('📥 Slow request started');
    
    // Simulate long processing
    await new Promise(resolve => setTimeout(resolve, 8000));
    
    console.log('✅ Slow request finished');
    res.json({ message: 'Finished after 8 seconds!' });
});

app.get('/cache/:key', async (req, res) => {
    try {
        const value = await redisClient.get(req.params.key);
        res.json({ key: req.params.key, value: value || 'not found' });
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});

app.post('/cache/:key/:value', async (req, res) => {
    try {
        await redisClient.set(req.params.key, req.params.value);
        res.json({ message: 'Cached successfully' });
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});

// Graceful shutdown handler
async function gracefulShutdown(signal) {
    console.log(`\n🛑 ${signal} received. Starting graceful shutdown...`);
    
    isShuttingDown = true;
    
    // Stop accepting new connections
    server.close(async () => {
        console.log('✅ HTTP server closed (no new requests accepted)');
        
        // Close Redis connection
        if (redisClient) {
            await redisClient.quit();
            console.log('✅ Redis connection closed');
        }
        
        console.log('✅ Graceful shutdown complete. Exiting...');
        process.exit(0);
    });
    
    // Force shutdown after 15 seconds if graceful shutdown fails
    setTimeout(() => {
        console.error('⚠️  Graceful shutdown timeout. Forcing exit...');
        process.exit(1);
    }, 15000);
}

// Handle signals
process.on('SIGTERM', () => gracefulShutdown('SIGTERM'));
process.on('SIGINT', () => gracefulShutdown('SIGINT'));

// Start server
async function start() {
    try {
        await connectRedis();
        
        server = app.listen(PORT, '0.0.0.0', () => {
            console.log(`🚀 Server running on port ${PORT}`);
        });
    } catch (err) {
        console.error('Failed to start server:', err);
        process.exit(1);
    }
}

start();
