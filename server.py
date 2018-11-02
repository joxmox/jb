from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import os
import json

from game import Games

class JbHandler(BaseHTTPRequestHandler):

    suff_2_ctype = {
        'html' : 'text/html',
        'js' : 'application/javascript',
        'css' : 'text/css',
        'jpg' : 'image/jpeg',
        'gif' : 'image/gif',
        'png' : 'image/png',
        'svg' : 'image/svg',
        'ico' : 'image/x-icon',
    }

    games = Games()

    def prelude(self):
        print(self.path)
        path = self.path
        if len(path) > 0 and path[0] == '/':
            path = path[1:]
        if len(path) > 0 and path[-1] == '/':
            path = path[:-1]
        self.pat = path.split('/')
        status = True
        if 'Content-Length' in self.headers:
            buff_len = int(self.headers['Content-Length'])
            if buff_len > 0:
                buffer = self.rfile.read(buff_len)
                try:
                    self.data = json.loads(buffer)
                except ValueError as err:
                    self.respond(400, txt='cannot read json data')
                    status = False
            else:
                self.data = {}
        else:
            self.data = {}
        if self.data:
            self.data['ip'] = self.client_address[0]
        return status

    def respond(self, code=200, ctype='text/html', data=None):
        print "respond", data
        self.send_response(code)
        if ctype is not None:
            self.send_header('Content-Type', ctype)
        if data:
            jdata = json.dumps(data)
            self.send_header('Content-Length', len(jdata))
        self.end_headers()
        if data:
            print jdata
            self.wfile.write(jdata)



    def serve_file(self, file):
        print ("serving file", file)
        if os.path.exists(file):
            if '.' in file:
                suff = (file + '.').split('.')[-2]
            else:
                suff = None
            ctype = JbHandler.suff_2_ctype.get(suff, 'text/html')
            self.respond(200, ctype=ctype)
            with open(file) as fh:
                self.wfile.write(fh.read())
        else:
            self.respond(404)

    def api_get(self):
        if len(self.pat) == 2 and self.pat[0] == 'game':
            data = JbHandler.games.next(self.pat[1])
            print data
            self.respond(200, data=data)
        else:
            self.respond(404)

    def api_post(self):
        print "post", self.pat
        if len(self.pat) == 1 and self.pat[0] == 'game':
            self.respond(200, data=JbHandler.games.new(self.data))
        else:
            self.respond(404)

    def do_GET(self):
        if not self.prelude():
            return
        print ("pat", self.pat)
        if self.pat == ['']:
            self.pat = ['index.html']
        if len(self.pat) == 1:
            self.serve_file(self.pat[0])
        else:
            if self.pat[0] == 'api':
                self.pat.pop(0)
                self.api_get()
            else:
                self.respond(404)

    def do_POST(self):
        if not self.prelude():
            return
        if len(self.pat) > 1 and self.pat[0] == 'api':
            self.pat.pop(0)
            self.api_post()
        else:
            self.respond(404)


class JbServer(object):

    def __init__(self, port):
        self.httpd = HTTPServer(('', port), JbHandler)

    def start(self):
        self.httpd.serve_forever()
