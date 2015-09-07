#!/usr/bin/env python
# coding=utf-8

import tornado.web
import datetime
import os
from base import BaseHandler
from hashlib import *
from umysql import *


class EntryHandler(BaseHandler):    #注册登录共用一个handler
    def get(self):
        self.render("login.html")    
        
    def post(self):
        user_sign = self.get_argument("username_sign")
        password_sign = self.get_argument("password_sign")
        user_email_sign = self.get_argument("email_sign")
        user_salt_sign = os.urandom(64)
              
        try:
            with db.transaction():
                user = User.create(
                    user_name = user_sign ,
                    user_salt = user_salt_sign ,
                    user_email = user_email_sign,
                    user_time   = datetime.datetime.now()
        )
            
        except IntegrityError as e:
            print e

        self.render("index.html",username_sign = user_sign)

