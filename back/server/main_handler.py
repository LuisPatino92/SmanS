from http.server import BaseHTTPRequestHandler
from urllib.parse import unquote_plus

import pdb

class CustomHandler(BaseHTTPRequestHandler):

    def get_payload(self):
        length = int(self.headers["Content-Length"])
        raw_content = self.rfile.read(length).decode("utf-8")
        data = {}
        for token in raw_content.split("&"):
            clean_content = unquote_plus(token)
            key, value = clean_content.split("=", 1)
            data.update({key: value})

        return data


    def do_POST(self):
        data = self.get_payload()
        pdb.set_trace()

        #TODO: Implement payload management