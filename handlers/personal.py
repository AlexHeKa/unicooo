#!/usr/bin/env python
# coding=utf-8

import tornado.web
from datetime import date
from umysql import *


class PublicHandler(BaseHandler):
    def get(self):
        username =       #正则获取用户名参数，活动名参数
        activity = 

    #获取活动的题目，内容，缩略图，类型等
    #该活动下的帖子id,帖子内容,帖子url，帖子所追随的活动，帖子统计数目等
    actinfos = Act.select(act_title,act_content,act_thumb_url,act_star,act_status,act_url,act_date_gmt,).where(Act.act_type == 0).sort by time

    
   actinfos 
    
   

