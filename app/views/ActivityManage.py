#!/usr/bin/env python
# encoding: utf-8
"""
@author: leason
@time: 2017/9/13 11:13
"""

import app.conf.msg as MSG
from app.untils import get_params
from app.framework_api import route, build_ret
from app.services.api import ActivityService


# admin活动操作
# 增加
@route("/admin/activity/add", api="activity", methods=['GET', 'POST'])
def activity_add():
    params = get_params()
    result = ActivityService.service_activity_add(params)
    msg = (MSG.SUCCESS.msg if result else MSG.FAIL.msg)
    return build_ret(success=result, msg=msg)


# 编辑
@route("/admin/activity/modify", api="activity", methods=['GET', 'POST'])
def activity_modify():
    params = get_params()
    result = ActivityService.service_activity_modify(params)
    return build_ret(success=result)


# 查询
@route("/admin/activity/list", api="activity", methods=['GET', 'POST'])
def activity_list():
    params = get_params()
    result, total = ActivityService.service_activity_list(params)
    return build_ret(success=True, data=result, total=total)


# 删除
@route("/admin/activity/del", api="activity", methods=['GET', 'POST'])
def activity_del():
    params = get_params()
    result = ActivityService.service_activity_del(params['id'])
    return build_ret(success=result)


# 详情
@route("/admin/activity/detail", api="activity", methods=['GET', 'POST'])
def activity_detail():
    params = get_params()
    result = ActivityService.service_activity_detail(params['id'])
    return build_ret(success=result, data=result)


# app活动接口
# 查询
@route("/app/activity/list", api="activity", methods=['GET', 'POST'])
def app_activity_list():
    params = get_params()
    result, total = ActivityService.service_activity_list(params)
    return build_ret(success=True, data=result, total=total)


# 详情
@route("/app/activity/detail", api="activity", methods=['GET', 'POST'])
def app_activity_detail():
    params = get_params()
    result = ActivityService.service_activity_detail(params['id'])
    return build_ret(success=result, data=result)