FROM node:18-alpine

WORKDIR /app

# Install dependencies
COPY package.json /app/package.json
COPY package-lock.json* /app/  # optional
RUN npm install

# Copy application code
COPY . /app

RUN npm run build

EXPOSE 3000

CMD ["npm", "run", "start"]