# Use the official Nginx image as a parent image
FROM nginx:alpine

# Remove the default Nginx configuration file
RUN rm /etc/nginx/conf.d/default.conf

# Copy a new configuration file from your project
COPY nginx.conf /etc/nginx/conf.d
