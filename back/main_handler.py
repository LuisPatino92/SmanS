from http.server import BaseHTTPRequestHandler
from urllib.parse import unquote_plus


class CustomHandler(BaseHTTPRequestHandler):

    def get_payload(self):
        length = int(self.headers["Content-Length"])
        raw_content = self.rfile.read(length)
        clean_content = unquote_plus(raw_content.decode("utf-8"))
        key, value = clean_content.split("=", 1)

        return {key: value}


    def do_POST(self):
        data = self.get_payload()

        #TODO: Implement payload management