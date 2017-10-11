#!/usr/bin/env python
# encoding: utf-8
"""
@author: WL
@time: 2017/10/11 10:41
"""
from app.conf import redis_pool_configs
import redis
redis_config = redis_pool_configs


def engine():
    configs = dict()
    configs['host'] = redis_config['host']
    configs['port'] = redis_config['port']
    configs['max_connections'] = redis_config['pool_size']
    pool = redis.ConnectionPool(**configs)
    if redis_config['password'] == '':
        r = redis.StrictRedis(connection_pool=pool)
    else:
        r = redis.StrictRedis(connection_pool=pool, password=redis_config['password'])
    return r

