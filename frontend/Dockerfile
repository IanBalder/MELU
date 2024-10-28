# Use an official Node runtime as a parent image
FROM node:18

# Set the working directory in the container
WORKDIR /app

# Copy package.json and install dependencies
COPY package*.json ./
RUN npm install

# Copy the rest of the application code
COPY . .

# Expose port 8080 for the Vue.js app
EXPOSE 8080

# Run the Vue.js development server
CMD ["npm", "run", "serve"]

