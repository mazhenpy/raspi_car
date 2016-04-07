# coding=utf-8
import os

import tornado.gen
import tornado.httpclient
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from handlers.motor import MotorHandler
from handlers.servo import ServoHandler


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('raspi_car.html')


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            (r"/servo", ServoHandler),
            (r"/motor", MotorHandler),
        ]
        settings = {
            "template_path": os.path.join(os.path.dirname(__file__), 'templates'),
            "static_path": os.path.join(os.path.dirname(__file__), "static"),
            "debug": False,
        }
        tornado.web.Application.__init__(self, handlers, **settings)
        self.port = 8003


if __name__ == '__main__':
    application = Application()
    print("http://127.0.0.1:{0}/".format(application.port))
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(application.port)
    tornado.ioloop.IOLoop.instance().start()
