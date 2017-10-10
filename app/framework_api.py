#!/usr/bin/env python
# encoding: utf-8
"""
@author: WL
@time: 2017/8/26 17:05
"""
from lib.decorators import route
from lib.utils import build_ret
from lib.utils.common import get_ret
from lib.utils.common import date_time
from lib.db import db

redis_service = db['redis']

