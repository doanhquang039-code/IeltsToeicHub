import http.server
import socketserver
import sys

class NoCacheHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

    # Prevent 304 responses to ensure browser always gets fresh content
    def send_error(self, code, message=None, explain=None):
        super().send_error(code, message, explain)

PORT = 8080

class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True

if __name__ == '__main__':
    with ReusableTCPServer(("", PORT), NoCacheHTTPRequestHandler) as httpd:
        print(f"Serving HTTP on port {PORT} (no-cache enabled)...")
        sys.stdout.flush()
        httpd.serve_forever()
