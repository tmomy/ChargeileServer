#!/usr/bin/env python
# encoding: utf-8
"""
@author: leason
@time: 2017/9/22 10:43
"""
from app.untils import get_params
from app.framework_api import route, build_ret, get_ret
from app.services.api import AppVersionService


# admin添加版本信息
@route("/admin/version/add", api="version", methods=['GET', 'POST'])
def version_add():
    params = get_params()
    state, result = AppVersionService.service_version_add(params)
    if state:
        return build_ret(result)
    return get_ret(result)


# 编辑
@route("/admin/version/modify", api="version", methods=['GET', 'POST'])
def version_modify():
    params = get_params()
    state, result = AppVersionService.service_version_modify(params)
    if state:
        return build_ret(result)
    return get_ret(result)


# 查询
@route("/admin/version/list", api="version", methods=['GET', 'POST'])
def version_list():
    params = get_params()
    result, total = AppVersionService.service_version_list(params)
    return build_ret(success=True, data=result, total=total)


# 删除
@route("/admin/version/del", api="version", methods=['GET', 'POST'])
def version_del():
    params = get_params()
    state, result = AppVersionService.service_version_del(params['id'])
    if state:
        return build_ret(result)
    return get_ret(result)


# app查询
@route("/app/version/list", type=True, api="version", methods=['GET', 'POST'])
def app_version_list():
    params = get_params()
    result = AppVersionService.service_version_app_list(params)
    return build_ret(success=True, data=result, total=0)
