#!/usr/bin/env python
# encoding: utf-8
"""
@author: WL
@time: 2017/10/11 15:42
"""
from sqlalchemy import (Column, Integer, String, DateTime)
from sqlalchemy.ext.declarative import declarative_base
from app.db.db_api import Engine
from datetime import datetime
ModelBase = declarative_base()


class LoginTable(ModelBase):
    __tablename__ = "login_table"
    id = Column(Integer, primary_key=True)
    username = Column(String(length=30), unique=True)
    create_time = Column(DateTime, default=datetime.now())
    expires = Column(DateTime, default=datetime.now())

    def __init__(self, username):
        self.username = username

    def to_json(self):
        return {
            'id': self.id,
            'username': self.name,
            'create_time': self.cate_time,
            'expires': self.expires
        }
