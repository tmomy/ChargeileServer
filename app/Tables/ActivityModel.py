#!/usr/bin/env python
# encoding: utf-8
"""
@author: leason
@time: 2017/9/13 9:02
"""
from sqlalchemy import (Column, Integer, String, DateTime)
from app.framework_api import date_time
from app.services.untils import ModelBase


class Activity(ModelBase):
    __tablename__ = "activity"
    __table_args__ = {
        'mysql_auto_increment': '0000'
    }
    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(Integer, nullable=False)  # 活动类型，暂定
    enable = Column(Integer, default=1, nullable=False)  # 0/1 启用 停用
    title = Column(String(100))
    desc = Column(String(300))
    pic = Column(String(300))
    url = Column(String(100))
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    create_time = Column(DateTime, default=date_time())

    def __init__(self, type, enable, title, desc, pic, url, start_time, end_time):
        self.type = type
        self.enable = enable
        self.desc = desc
        self.title = title
        self.pic = pic
        self.url = url
        self.start_time = start_time
        self.end_time = end_time

    def to_json(self):
        return {
            'id': self.id,
            'type': self.type,
            'enable': self.enable,
            'desc': self.desc,
            'title': self.title,
            'url': self.url,
            'pic': self.pic,
            'start_time': str(self.start_time),
            'end_time': str(self.end_time),
            'create_time': str(self.create_time)
        }

    def to_json_list(self):
        return {
            'id': self.id,
            'type': self.type,
            'enable': self.enable,
            'desc': self.desc,
            'title': self.title,
            'url': self.url,
            'pic': self.pic,
            'start_time': str(self.start_time),
            'end_time': str(self.end_time),
            'create_time': str(self.create_time)
        }

    def __repr__(self):
        return "<id={},title={},url={}>".format(self.id, self.title, self.url)
