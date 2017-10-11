#!/usr/bin/env python
# encoding: utf-8
"""
@author: WL
@time: 2017/8/25 9:52
"""
from lib.flask import app
from app.untils.log_builder import sys_logging as logging


@app.after_request
def response_handler(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type,authorization'
    response.headers['Access-Control-Expose-Headers'] = "authorization"
    logging.info("response is [{}]".format(response.data))
    return response

