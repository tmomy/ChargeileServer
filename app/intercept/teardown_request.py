#!/usr/bin/env python
# encoding: utf-8
"""
@author: WL
@time: 2017/10/11 15:16
"""
from lib.flask import app
from flask import g
from sqlalchemy import exc


@app.teardown_request
def session_close(exception):
    print 222
    g.session.close()

