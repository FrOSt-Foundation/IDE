import logging
import os
import re

import tornado.escape
import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.gen

from tornado.options import define, options, parse_command_line

define("port", default=8080, help="run on the given port", type=int)
define("debug", default=True, help="run in debug mode")

class MainHandler(tornado.web.RequestHandler):
    def get(self, doc_uuid=""):
        logging.info("index with (uuid: %s)" % doc_uuid)

        self.render("index.html", uuid=doc_uuid)

def main():
    parse_command_line()
    settings = dict(
            cookie_secret="SjDi8fx34rDF3",
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            xsrf_cookies=True,
            debug=options.debug
        )
    handlers = [
            (r"/", MainHandler),
            (r"/static/(.*)", tornado.web.StaticFileHandler, {"path" : settings["static_path"]})
        ]
    app = tornado.web.Application(handlers, **settings)
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()
