# encoding: utf-8

"""
@version: 1.0
@author: dawning
@contact: dawning7670@gmail.com
@time: 2017/3/22 16:01
"""
from ConfigService import (online_config, local_config)
CONF_MAP = {
    'online': online_config,
    'local': local_config
}

ENVIRONMENT = 'online'

config = CONF_MAP[ENVIRONMENT]
