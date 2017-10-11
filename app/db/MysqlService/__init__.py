#!/usr/bin/env python
# encoding: utf-8
"""
@author: WL
@time: 2017/10/10 15:37
"""
from Pools import Engine
from sqlalchemy.orm import sessionmaker
session_factory = sessionmaker(bind=Engine)