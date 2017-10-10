#!/usr/bin/env python
# encoding: utf-8
"""
@author: WL
@time: 2017/9/8 15:01
"""
from sqlalchemy import (Column, Integer, String, Text, DateTime, ForeignKey)
from app.framework_api import date_time
from app.services.untils import ModelBase
# <-元类


class Message(ModelBase):
    __tablename__ = "message"
    __table_args__ = {
        'mysql_auto_increment': '0000'
    }
    id = Column(Integer, primary_key=True, autoincrement=True)
    message_type = Column(Integer, nullable=False)  # 123 系统消息、呱呱公告、呱呱优惠
    type = Column(Integer, nullable=False)  # 0/1 广播、私信
    status = Column(Integer, default=1, nullable=False)  # 0/1 已推送、未推送
    title = Column(String(100))
    desc = Column(Text)
    waiter_id = Column(Integer)
    reply_id = Column(Integer)
    pic = Column(String(100))
    detail = Column(Text)
    user_id = Column(Integer, ForeignKey('user.user_id'))
    effect_time = Column(DateTime)
    create_time = Column(DateTime, default=date_time())

    def __init__(self, waiter_id, message_type, type, title, detail, user_id, effect_time=date_time(), desc=None, pic=None, reply_id=None):
        self.waiter_id = waiter_id
        self.title = title
        self.message_type = message_type
        self.type = type
        self.detail = detail
        self.user_id = user_id
        self.reply_id = reply_id
        self.desc = desc
        self.pic = pic
        self.create_time = date_time()
        self.effect_time = effect_time

    def to_json(self):
        return {
            'id': self.id,
            'message_type': self.message_type,
            'title': self.title,
            'status': self.status,
            'detail': self.detail,
            'waiter_id': self.waiter_id,
            'reply_id': self.reply_id,
            'user_id': self.user_id,
            'desc': self.desc,
            'pic': self.pic,
            'create_time': str(self.create_time),
            'effect_time': str(self.effect_time)
        }

    def to_json_list(self):
        return {
            'id': self.id,
            'message_type': self.message_type,
            'title': self.title,
            'status': self.status,
            'reply_id': self.reply_id,
            'user_id': self.user_id,
            'desc': self.desc,
            'pic': self.pic,
            'create_time': str(self.create_time),
            'effect_time': str(self.effect_time)
        }

    def __repr__(self):
        return "<id={},message_type={},user_id={}>".format(self.id, self.message_type, self.user_id)