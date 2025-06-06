# filename: app.py

from http.server import BaseHTTPRequestHandler, HTTPServer

# HTML content stored as a string inside the Python file
HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Embedded HTML</title>
</head>
<body>
    <h1>Hello from inside a .py file!</h1>
    <p>This HTML is stored directly in Python.</p>
</body>
</html>
"""

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(HTML_PAGE.encode())

if __name__ == '__main__':
    server = HTTPServer(('localhost', 8000), MyHandler)
    print("Server started at http://localhost:8000")
    server.serve_forever()



