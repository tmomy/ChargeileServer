#!/usr/bin/env python
# encoding: utf-8
"""
@author: WL
@time: 2017/10/11 17:09
"""
from app.framework_api import route, build_ret
from app.services.api import TableInitService


@route("/admin/table/create", type=True, api="后台管理系统登录", methods=['GET'])
def table_create():
    TableInitService.create_table_api()
    return build_ret(success=True, msg="ok!")


@route("/admin/table/drop", type=True, api="后台管理系统登录", methods=['GET'])
def table_drop():
    TableInitService.drop_table_api()
    return build_ret(success=True, msg="ok!")