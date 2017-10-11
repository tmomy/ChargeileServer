# encoding: utf-8

"""
@version: 1.0
@author: dawning
@contact: dawning7670@gmail.com
@time: 2017/3/22 16:01
"""
ENVIRONMENT = False
if ENVIRONMENT:
    from ConfigService.online_config import *
else:
    from ConfigService.local_config import *
