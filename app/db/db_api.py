#!/usr/bin/env python
# encoding: utf-8
"""
@author: WL
@time: 2017/10/11 11:03
"""
from MysqlService import session_factory, Engine
from RedisService.Pools import engine
"""
该模块负责提供系统支持的数据库对应连接池API
"""

# redis
rdc = engine()
