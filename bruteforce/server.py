from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse as parser

class ServerHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()

        f = open("index.html", 'r')
        data = f.read()
        f.close()
        self.wfile.write(data.encode())

        '''
        self.wfile.write('<p>GET</p>'.encode())
        print('GET Requests')
        self.wfile.write(self.path.encode())
        self.wfile.write('<br/><br/>'.encode())
        if '?' in self.path:
            self.wfile.write(str(self.path.split('?')[1].split('&'))
                             .encode())
        print(parser.parse_qsl(self.path.split('?')[1]))
        print(dict(parser.parse_qsl(self.path.split('?')[1])))
        '''

    def do_POST(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        print('POST Requests')
        '''
        self.wfile.write('<p>POST</p>'.encode())
        self.wfile.write(self.path.encode())
        self.wfile.write('<br/><br/>'.encode())
        '''
        data = self.rfile.read(int(self.headers['Content-Length']))
        if data is not None:
            data_decode = dict(parser.parse_qs(data.decode()))
        if data_decode['id'] == ['seona'] and data_decode['pw'] == ['1234']:
            self.wfile.write('login success'.encode())
        else:
            f = open("index_fail.html", 'r')
            data = f.read()
            f.close()
            self.wfile.write(data.encode())
        print(f'post params = {data_decode}')

PORT = 8080
server = HTTPServer(('', PORT), ServerHandler)
print(f'서버 {PORT}로 서비스 진행 중.')
server.serve_forever()
