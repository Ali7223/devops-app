from http.server import BaseHTTPRequestHandler, HTTPServer
import os

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        message = os.getenv("MESSAGE", "Default Message")
        self.wfile.write(message.encode())
        self.wfile.write("Hello from CI-CD Pipeline 🚀".encode())

HTTPServer(('0.0.0.0', 8080), Handler).serve_forever()
