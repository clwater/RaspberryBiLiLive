import socket

import tornado.ioloop
import tornado.web
import Info


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        ip = ''
        with open('ip' , 'r') as f:
            ip = f.read()

        print ip
        urlp = 'http://' + ip + ':10002'

        print urlp

        self.redirect(urlp)


class MainHandlerChange(tornado.web.RequestHandler):
    def get(self):
        ips = self.get_argument("ips", None)
        with open('ip', 'w') as f:
            f.write(ips)
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

runServer()
