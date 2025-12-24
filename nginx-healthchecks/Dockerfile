FROM nginx:alpine

WORKDIR /app

COPY index.html /usr/share/nginx/html

# add health check
HEALTHCHECK --interval=5s --timeout=3s --retries=3 \
    CMD curl -f http://localhost/ || exit 1
EXPOSE 80