#!/usr/bin/env python
# coding=utf-8

import tornado.web
from datetime import date
from umysql import *


class ActivityHandler(BaseHandler):
    @tornado.web.authenticated
    edit = False;
    def get(self):
        username =       #正则获取用户名参数，活动名参数
        activity = 
        current_user = get_current_user()
        if username = current_user:
            edit = True;

    #获取活动的题目，内容，缩略图，类型等
    #该活动下的帖子id,帖子内容,帖子url，帖子所追随的活动，帖子统计数目等
    actinfos = Act.select(act_title,act_content,act_thumb_url,act_type,act_star,act_status,act_date_gmt).join(User).where(User.user_name == username and Act.act_alias == activity)
    postinfos = Post.select().where(Act.act_title == activity)
    
    
    act_title = actinfos[0]
    act_content = actinfos[1]
    act_thumb_url = actinfos[2]
    act_type = actinfos[3]
    act_star = actinfos[4]
    act_status = actinfos[5]
    act_date_gmt = actinfos[6]

    post_content = postinfos[0]
    post_thumb_url = postinfos[1]
    post_likes_count = postinfos[2]
    post_comments_count = postinfos[3]

    self.render("/username",username=username,uid=uid,user_portrait=user_portrait,user_message=user_message,post_content=post_content,post_thumb_url=post_thumb_url,post_likes_count=post_likes_count,post_comments_count=post_comments_count)



