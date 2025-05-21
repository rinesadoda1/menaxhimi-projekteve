from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello from AWS EC2 Python app!")

httpd = HTTPServer(("0.0.0.0", 8080), SimpleHandler)
print("Server listening on port 8080...")
httpd.serve_forever()
