#!/usr/bin/env python
# encoding: utf-8
"""
@author: WL
@time: 2017/7/27 20:22
"""
from sqlalchemy import create_engine, exc
from sqlalchemy.pool import QueuePool
from app.untils.log_builder import pool_logging
from app.conf import mysql_pool_configs


def engine():
    db_pool = None
    try:
        db_pool = create_engine(mysql_pool_configs['url'], poolclass=QueuePool,
                                pool_size=mysql_pool_configs['pool_size'],
                                max_overflow = mysql_pool_configs['max_overflow'],
                                pool_recycle = mysql_pool_configs['pool_recycle']
                                )
    except exc.OperationalError as e:
        pool_logging.debug("create pool err:", e)
    return db_pool
Engine = engine()







