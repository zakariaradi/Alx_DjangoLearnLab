# HTTPS Deployment Configuration

To enable HTTPS in production, the application must be served behind
a web server configured with SSL/TLS certificates.

## Example (Nginx)

1. Obtain an SSL certificate (e.g., via Let's Encrypt).
2. Configure Nginx to listen on port 443 with SSL enabled.
3. Redirect all HTTP (port 80) traffic to HTTPS.

Example configuration snippet:

server {
    listen 80;
    server_name example.com;
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl;
    server_name example.com;

    ssl_certificate /etc/ssl/certs/fullchain.pem;
    ssl_certificate_key /etc/ssl/private/privkey.pem;

    location / {
        proxy_pass http://localhost:8000;
    }
}

This ensures all traffic is encrypted and served securely over HTTPS.
