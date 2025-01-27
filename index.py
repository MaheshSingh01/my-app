import json
from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs

# Load marks data from the JSON file
with open("q-vercel-python.json", "r") as f:
    data = json.load(f)

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse query parameters
        query = parse_qs(self.path[2:])
        names = query.get("name", [])
        
        # Find marks for the given names
        response = {"marks": [student["marks"] for student in data if student["name"] in names]}
        
        # Enable CORS
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        
        # Send the response
        self.wfile.write(json.dumps(response).encode("utf-8"))
        return
