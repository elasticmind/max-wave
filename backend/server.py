from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import wave_heights


class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_POST(self):
        body = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
        wave_height = wave_heights.get_wave_height_at(body['lng'], body['lat'])
        self._set_headers()
        self.wfile.write(str(wave_height).encode("utf8"))


def run(server_class=HTTPServer, handler_class=S, addr="localhost", port=8000):
    httpd = server_class((addr, port), handler_class)
    print(f"Server listening on {addr}:{port}...")
    httpd.serve_forever()


if __name__ == "__main__":
    run()