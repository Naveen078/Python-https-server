from http.server import HTTPServer, BaseHTTPRequestHandler 
import ssl

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")

httpd = HTTPServer(('0.0.0.0', 8002), BaseHTTPRequestHandler)
httpd.socket = ssl_context.wrap_socket(httpd.socket, server_side=True)

try:
    print("Server Started. Listening on https://0.0.0.0:8002/")
    httpd.serve_forever()
except KeyboardInterrupt:
    print("\nServer Shutting Down. Goodbye!")
