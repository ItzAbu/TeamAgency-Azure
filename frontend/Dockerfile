# Stage 1: build
FROM node:18-alpine AS builder

WORKDIR /app

COPY package*.json ./
RUN npm install --production=false
COPY . .
RUN npm run build

# Stage 2: serve
FROM nginx:alpine

COPY --from=builder /app/build /usr/share/nginx/html

ENV PORT=80

EXPOSE ${PORT}

# Healthcheck: verifica se nginx serve la homepage
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 CMD wget --spider -q http://localhost:${PORT}/ || exit 1

CMD ["nginx", "-g", "daemon off;"]