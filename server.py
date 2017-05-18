#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    File:     server.py
    Version:  0.0.1
    Author:   miao
    Email:    miao@miao.com
    Date:     18/05/2017 17:34
    Copy:     Copyright 2017, miao.com
"""

import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
