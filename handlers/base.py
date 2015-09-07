#! /usr/bin/env python
# coding=utf-8

import tornado.web
import MySQLdb
from umysql import *

class BaseHandler(tornado.web.RequestHandler):    
    def prepare(self):
        db.connect()
        return super(BaseHandler, self).prepare()

    def on_finish(self):
        if not db.is_closed():
            db.close()
        return super(BaseHandler, self).on_finish()

    def get_current_user(self):
        return self.get_secure_cookie("username")

    def set_current_user(self, user):
        if user:
            self.set_secure_cookie('user', tornado.escape.json_encode(user))    #注意这里使用了tornado.escape.json_encode()方法
        else:
            self.clear_cookie("user")

