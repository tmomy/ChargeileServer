#!/usr/bin/env python
# encoding: utf-8
"""
@author: WL
@time: 2017/9/11 16:16
"""
from app.untils import get_params
from app.framework_api import route, build_ret, get_ret
from app.services.api import UserInfoService


@route("/account/login_name/operation", api="绑定手机号修改", methods=['GET', 'POST'])
def account_modify():
    params = get_params()
    opr = params['opr']
    if opr == "add":
        data = params['data']
        mobile = data.get("mobile")
        valid_type = data.get('type')
        if valid_type is None:
            valid_type = "original"
        re_bool, result = UserInfoService.account_send_api(mobile=mobile, valid_type=valid_type)
        return get_ret(result)
    elif opr == "modify":
        data = params['data']
        code = data.get('code')
        mobile = data.get("mobile")
        valid_type = data.get('type')
        if valid_type is None:
            valid_type = "original"
        re_bool, result = UserInfoService.account_valid_api(code=code, mobile=mobile, valid_type=valid_type)
        return get_ret(result)
    else:
        return build_ret(success=True, msg="该接口还未开放！", code=404)


@route("/account/info", api="会员信息模块", methods=['GET', 'POST'])
def account_info():
    params = get_params()
    opr = params['opr']
    if opr == "search":
        re_bool, result = UserInfoService.account_info_api()
        if re_bool:
            return build_ret(success=True, data=result)
        return get_ret(result)
    elif opr == "modify":
        data = params['data']
        field = data.get('field')
        value = data.get('value')
        re_bool, result = UserInfoService.account_edit_api(field=field, value=value)
        return get_ret(result)
    else:
        return build_ret(success=True, msg="该接口还未开放！", code=404)


@route("/account/password", type=True, api="密码修改", methods=['GET', 'POST'])
def password_modify():
    params = get_params()
    opr = params['opr']
    if opr == "modify":
        mobile = params['data']['mobile']
        password = params['data']['password']
        re_bool, result = UserInfoService.password_edit_api(password=password, mobile=mobile)
        return get_ret(result)
    else:
        return build_ret(success=True, msg="该接口还未开放！", code=404)


@route("/account/password/sms", type=True, api="密码修改-验证码", methods=['GET', 'POST'])
def password_modify():
    params = get_params()
    opr = params['opr']
    if opr == "add":
        mobile = params['data']['mobile']
        re_bool, result = UserInfoService.password_send_api(mobile=mobile)
        return get_ret(result)
    elif opr == "modify":
        code = params['data']['code']
        mobile = params['data']['mobile']
        re_bool, result = UserInfoService.passowrd_valid_api(code=code, mobile=mobile)
        return get_ret(result)
    else:
        return build_ret(success=True, msg="该接口还未开放！", code=404)