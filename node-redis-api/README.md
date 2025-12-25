Built Node.js API with Redis implementing graceful shutdown handling via SIGTERM signals in application code. 

Prevents data loss and user errors during deployments - when SIGTERM arrives during active requests, the app stops accepting new requests (503) but finishes all active ones before exiting. 

Tested with 8-second slow endpoint: SIGTERM arrived at 2s, app waited 6 more seconds to complete request, then closed Redis connection and exited cleanly with code 0.