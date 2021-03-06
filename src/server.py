#!/usr/bin/python
# -*- coding: UTF-8 -*-

import socket

import tornado.ioloop
import tornado.web



class MainHandler(tornado.web.RequestHandler):
    def get(self):
        from ScanFile import scan
        fileList = scan()
        self.render('index.html' , files = fileList)

class MainHandlerChange(tornado.web.RequestHandler):
    def get(self):
        streamname  = self.get_argument("streamname", None)
        key  = self.get_argument("key", None)



        with open('streamname', 'w') as f:
            f.write(streamname)
        with open('key', 'w') as f:
            f.write(key)

        self.write('streamname =' + streamname + ' key = ' + key)

class MainHandlerIndex(tornado.web.RequestHandler):
    def get(self):
        index = self.get_argument("index", '')
        self.render('show.html', file=index)

        print 'index' + index
        from PushFile import pushFile
        pushFile(index)


application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/index", MainHandlerIndex),
    (r"/ad" , MainHandlerChange)

])


def runServer():
    port = 7701
    application.listen(port)

    localIP = socket.gethostbyname(socket.gethostname())
    print("run in %s:%s"%(localIP,port))
    tornado.ioloop.IOLoop.instance().start()

