# --- Stage 1: build ---
FROM node:20 AS build
WORKDIR /app
COPY package.json .
RUN npm install
COPY server.js .

# --- Stage 2: run (slim final image) ---
FROM node:20-slim
WORKDIR /app
COPY --from=build /app /app
EXPOSE 3000
CMD ["node", "server.js"]
