#!/usr/bin/env python
# encoding: utf-8
"""
@author: WL
@time: 2017/10/11 17:00
"""
from app.db.MysqlService import Engine
from sqlalchemy.ext.declarative import declarative_base

ModelBase = declarative_base()
engine = Engine
