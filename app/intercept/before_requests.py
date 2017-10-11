#!/usr/bin/env python
# encoding: utf-8
"""
@author: WL
@time: 2017/10/11 14:42
"""
import json
from lib.flask import app
from lib.decorators import rules, login_list
from flask import g
from app.db.MysqlService import session_factory


@app.before_request
def mysql_session():
    g.session = session_factory()