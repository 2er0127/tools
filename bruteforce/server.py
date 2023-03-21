from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse as parser

class ServerHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        self.wfile.write('<p>GET</p>'.encode())
        print('GET Requests')
        self.wfile.write(self.path.encode())
        self.wfile.write('<br/><br/>'.encode())
        if '?' in self.path:
            self.wfile.write(str(self.path.split('?')[1].split('&'))
                             .encode())
        print(parser.parse_qsl(self.path.split('?')[1]))
        print(dict(parser.parse_qsl(self.path.split('?')[1])))

    def do_POST(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        self.wfile.write('<p>POST</p>'.encode())
        print('POST Requests')
        self.wfile.write(self.path.encode())
        self.wfile.write('<br/><br/>'.encode())
        data = self.rfile.read(int(self.headers['Content-Length']))
        if data is not None:
            data_decode = dict(parser.parse_qs(data.decode()))
        print(f'post params = {data_decode}')

PORT = 8080
server = HTTPServer(('', PORT), ServerHandler)
print(f'서버 {PORT}로 서비스 진행 중.')
server.serve_forever()
