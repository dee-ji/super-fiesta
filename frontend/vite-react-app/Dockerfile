# Stage 1: Build the React application
FROM node:16-alpine as build

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json (if available) to the working directory
COPY ./package*.json ./

# Install dependencies
# Note: It's important to install Vite globally to use the create command
RUN npm install

# Use the command to create a new Vite React app, bypass this step if your app is already set up
# and you are copying the existing source code into the image
# RUN npm create vite@latest vite-react-app -- --template react-ts

# Copy the existing app source code to the container
COPY . .

# Build the app for production
RUN npm run build

# Stage 2: Serve the app with Nginx
FROM nginx:alpine

# Copy the build output to replace the default nginx contents.
COPY --from=build /app/dist /usr/share/nginx/html

# Expose port 80 to the outside once the container has launched
EXPOSE 80

# Define the command to run your app using CMD which defines your runtime
CMD ["nginx", "-g", "daemon off;"]
