from http.server import  HTTPServer

from main_handler import CustomHandler


host = 'localhost'
port = 8000


server = HTTPServer((host, port), CustomHandler)

print(f"Server started at http://{host}:{port}")

# Start the server
server.serve_forever()