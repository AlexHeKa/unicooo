#!/usr/bin/env python
# coding=utf-8

import tornado.web
import tornado.escape
from base import *
import datetime


class IndexHandler(BaseHandler):
    def get(self):
       # if self.current_user is True:    #当获取到用户cookie时
       #     username = tornado.escape.json_decode(self.current_user)    #获取设置在cookie里面的用户名
       #     self.render("/",users=username)
       # else:
       #     self.render("/",users=login)     #如果没登录，二级导航显示注册登录
       self.render("index.html",username_sign = username_sign)
        


        
 
