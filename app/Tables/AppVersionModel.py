#!/usr/bin/env python
# encoding: utf-8
"""
@author: leason
@time: 2017/9/22 10:02
"""
from sqlalchemy import (Column, Integer, String, DateTime)
from app.framework_api import date_time
from app.services.untils import ModelBase


class AppVersion(ModelBase):
    __tablename__ = "app_version"

    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(Integer, nullable=False)      # 0 强制升级 1 不强制
    platform = Column(Integer, nullable=False)  # 0 android 1 ios
    desc = Column(String(length=250))
    version_number = Column(String(length=50), nullable=False)
    update_url = Column(String(length=250))
    enable = Column(Integer, nullable=False)  # 0 启用 1 禁用

    create_time = Column(DateTime)

    def __init__(self, type, version_number, platform, desc, update_url, enable):
        self.type = type
        self.version_number = version_number
        self.platform = platform
        self.desc = desc
        self.update_url = update_url
        self.enable = enable
        self.create_time = date_time()

    def to_json(self):

        return {
            'id': self.id,
            'type': self.type,
            'platform': self.platform,
            'version_number': self.version_number,
            'desc': self.desc,
            'update_url': self.update_url,
            'enable': self.enable,
            'create_time': str(self.create_time)
        }

    def __repr__(self):
        return "<id={},type={},platform={}>".format(self.id, self.type, self.platform)
