#!/usr/bin/env python
# coding=utf-8

import tornado.web
import tornado.escape
from base import BaseHandler


class LoginHandler(BaseHandler):    #注册登录共用一个handler
    def get(self):
        if self.current_user:    #当获取到用户cookie时
            username = tornado.escape.json_decode(self.current_user)    #获取设置在cookie里面的用户名
            self.redirect("/username",username=username)  #跳转到个人中心页面

    def post(self):
        username_sign = self.get_argument("username_sign")
        user_email_sign = self.get_argument("email_sign")
        password_sign = self.get_argument("password_sign")

        user_infos = [
        {'user_name': username_sign, 'user_email': user_email_sign},
        {'user_pass': password_sign, 'user_salt': xxx, 'user_registeredTime': xxxx}
        ]
        try:
            #尝试插入纪录到数据库User表 使用(peewee orm)
            with db.atomic():
            User.insert_many(user_infos).execute()
            self.set_current_user(username)
        except peewee.IntegrityError:
            #按照返回的错误来判断用户名重复还是email重复
            if xxx:
                return 1001
            else:
                return 1002

        username_login = self.get_argument("username_login")
        password_login = self.get_argument("password_login")
        
        try:
            userinfos = User.select(User.user_name,User.user_pass).where(User.user_name== username_login)
        except xxx: #没有这名用户
            if xxx:
                return 1003
            else:
                return 1004

        try:
            password_login == userinfos[1]
        except xxx: #密码错误
            if xxx:
                return 1005
            else xxx:
                return 1006

       
        def set_current_user(self, user):
        if user:
            self.set_secure_cookie('user', tornado.escape.json_encode(user))    #注意这里使用了tornado.escape.json_encode()方法
        else:
            self.clear_cookie("user")


