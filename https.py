from http.server import HTTPServer, BaseHTTPRequestHandler 
import ssl

# Create an SSL context
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")

# Create an HTTP server with the SSL context
httpd = HTTPServer(('0.0.0.0', 8002), BaseHTTPRequestHandler)
httpd.socket = ssl_context.wrap_socket(httpd.socket, server_side=True)

try:
    # Start serving forever
    print("Server Started. Listening on https://0.0.0.0:8002/")
    httpd.serve_forever()
except KeyboardInterrupt:
    # Handle Ctrl+C gracefully
    print("\nServer Shutting Down. Goodbye!")
