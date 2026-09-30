# Build stage
FROM node:18-alpine AS builder
WORKDIR /app

# Install dependencies
COPY package*.json ./
RUN npm ci

# Copy source code
COPY . .
# Build static export of Next.js app
RUN npm run build && npm run export

# Production stage: serve static content with a lightweight web server
FROM nginx:alpine AS production
COPY --from=builder /app/out /usr/share/nginx/html
# Optional: Copy custom nginx config if needed
# COPY nginx.conf /etc/nginx/nginx.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]