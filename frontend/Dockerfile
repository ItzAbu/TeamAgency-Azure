# multi-stage build per frontend produzione (se serve)
FROM node:18-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

FROM node:18-alpine AS production
WORKDIR /app
COPY --from=build /app/build ./build
COPY package*.json ./
RUN npm install --production
CMD ["npx", "serve", "-s", "build", "-l", "3000"]