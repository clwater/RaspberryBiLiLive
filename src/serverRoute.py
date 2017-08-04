import socket

import tornado.ioloop
import tornado.web
import Info

url = '0.0.0.0'

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        urlp = Info.ip + ':10002'
        self.redirect(urlp)

class MainHandlerChange(tornado.web.RequestHandler):
    def get(self):
        ips = self.get_argument("ips", None)
        Info.ip = ips
        self.write('keyi')


application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/change", MainHandlerChange),

])


def runServer():
    port = 11000
    application.listen(port)

    localIP = socket.gethostbyname(socket.gethostname())
    print("run in %s:%s"%(localIP,port))
    tornado.ioloop.IOLoop.instance().start()

