#!/usr/bin/env python
# coding=utf-8

import tornado.web
from datetime import date
from umysql import *


class UserHandler(BaseHandler):
    @tornado.web.authenticated
    edit = False
    def get(self):
        username =       #正则获取用户名参数
        current_user = get_current_user()
        if username = current_user:
            edit = True

    #获取用户名user_name，头像url地址user_portrait，用户简介user_message,
    #发布的帖子id,帖子内容,帖子url，帖子所追随的活动，帖子统计数目
    userinfos = User.select(uid,user_portrait,user_message).where(User.username == username)
    postinfos = Post.select(post_content,post_thumb_url,post_likes_count,post_comments_count).join(User).where(uid == userinfos[0])

    uid = userinfos[0]
    user_portrait = userinfos[1]
    user_message = userinfos[2]

    post_content = postinfos[0]
    post_thumb_url = postinfos[1]
    post_likes_count = postinfos[2]
    post_comments_count = postinfos[3]

    self.render("/username",username=username,uid=uid,user_portrait=user_portrait,user_message=user_message,post_content=post_content,post_thumb_url=post_thumb_url,post_likes_count=post_likes_count,post_comments_count=post_comments_count)


