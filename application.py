#!/usr/bin/env python
# coding=utf-8

from url import url

import tornado.web
import os

settings = dict(
    template_path = os.path.join(os.path.dirname(__file__), "templates"),
    static_path = os.path.join(os.path.dirname(__file__), "statics"),
    cookie_secret = "S3Gc7hooSGaevGi+zanE+t/7Njc1BU+xhb3jrRuKq4w=",
    )

application = tornado.web.Application(
    handlers = url,
    **settings
    )
