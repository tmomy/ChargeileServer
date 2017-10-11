#!/usr/bin/env python
# encoding: utf-8
"""
@author: WL
@time: 2017/9/7 10:04
"""
from flask import g
from app.untils import get_params
from app.framework_api import route, build_ret, get_ret
from app.Tables.TestDemo import LoginTable


@route("/admin/test", type=True, api="后台管理系统登录", methods=['GET', 'POST'])
def admin_login():
    params = get_params()
    print params
    username = params['username']
    se = g.session
    user = LoginTable(username=username)
    se.add(user)
    se.commit()
    return build_ret(success=True, msg="ok!")
