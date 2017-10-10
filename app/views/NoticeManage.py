#!/usr/bin/env python
# encoding: utf-8
"""
@author: leason
@time: 2017/9/12 9:10
"""
import app.conf.msg as MSG
from app.untils import get_params
from app.framework_api import route, build_ret, get_ret
from app.services.api import NoticeService
from app.untils.context_get import get_user_info


# admin通知操作
# 增加
@route("/admin/notice/add", api="notice", methods=['GET', 'POST'])
def notice_add():
    params = get_params()
    waiter_id = get_user_info()['user_id']
    params['waiter_id'] = waiter_id
    result = NoticeService.service_notice_add(params)
    msg = (MSG.SUCCESS.msg if result else MSG.FAIL.msg)
    return build_ret(success=result, msg=msg)


# 查询
@route("/admin/notice/list", api="notice", methods=['GET', 'POST'])
def notice_list():
    params = get_params()
    result, total = NoticeService.service_notice_list(params)
    return build_ret(success=True, data=result, total=total)


# 删除
@route("/admin/notice/del", api="notice", methods=['GET', 'POST'])
def notice_del():
    params = get_params()
    result = NoticeService.service_notice_del(params['id'])
    return build_ret(success=result)


# 详情
@route("/admin/notice/detail", api="notice", methods=['GET', 'POST'])
def notice_detail():
    params = get_params()
    result = NoticeService.service_notice_detail(params['id'])
    return build_ret(success=result, data=result)


# 极光推送
@route("/admin/notice/jpush", api="notice", methods=['GET', 'POST'])
def notice_jpush():
    params = get_params()
    state, result = NoticeService.service_notice_jpush(params['id'])
    if state:
        return build_ret(result)
    return get_ret(result)


# app通知操作
# 查询
@route("/app/notice/list", api="notice", methods=['GET', 'POST'])
def app_notice_list():
    params = get_params()
    params['cond']['login_name'] = get_user_info()['username']
    result, total = NoticeService.service_app_notice_list(params)
    return build_ret(success=True, data=result, total=total)


# 详情
@route("/app/notice/detail", type=True, api="notice", methods=['GET', 'POST'])
def app_notice_detail():
    params = get_params()
    result = NoticeService.service_notice_detail(params['id'])
    return build_ret(success=result, data=result)
