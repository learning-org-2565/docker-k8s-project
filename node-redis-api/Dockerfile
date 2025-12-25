FROM node:alpine AS builder
WORKDIR /app
COPY package.json .
RUN npm install

# STAGE 2 - Production Image
FROM node:alpine
WORKDIR /app
COPY --from=builder /app/node_modules ./node_modules
COPY server.js .
EXPOSE 3000
CMD ["node", "server.js"]

