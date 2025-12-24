
# Project 1: Production Nginx with Health Checks

## What We Built
- Custom Nginx container serving static HTML
- Health checks baked into image
- Resource limits applied

## Measurements
- Peak CPU: 3.31% under load
- Peak Memory: 3.1 MiB
- Limits set: 0.25 CPUs (25%), 64MB RAM

## Commands Used
```bash
# Build image
docker build -t nginx-health:v1 .

# Run with limits
docker run -d --name health-nginx \
  -p 8080:80 \
  --cpus="0.25" \
  --memory="64m" \
  nginx-health:v1

# Verify limits
docker stats health-nginx --no-stream
docker inspect health-nginx --format='{{.HostConfig.NanoCpus}}'
```

## Key Learnings
- Health checks in Dockerfile = automatic for all users
- Always measure FIRST, then set limits
- Production limits = peak usage + 50% buffer minimum