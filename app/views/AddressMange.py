#!/usr/bin/env python
# encoding: utf-8
"""
@author: WL
@time: 2017/9/5 14:34
"""
from app.untils import get_params
from app.framework_api import route, build_ret, get_ret
from app.services.api import AccountService


@route("/account/address/operation", api="系统初始化操作", methods=['GET', 'POST'])
def account_address():
    params = get_params()
    opr = params['opr']
    if opr == "add":
        address_info = params['data']
        _, result = AccountService.address_add_api(address_info=address_info)
        return get_ret(result)
    elif opr == "search":
        data = params['data']
        page = data.get('page')
        limit = data.get('limit')
        cond = data.get('cond')
        address_id = cond.get('id').strip()
        total, result = AccountService.address_search_api(address_id=address_id, page=page, limit=limit)
        if total is not False:
            return build_ret(success=True, total=total, data=result)
        else:
            return get_ret(result)
    elif opr == "modify":
        edit_info = params['data']
        re_bool, result = AccountService.address_edit_api(address_info=edit_info)
        return get_ret(result)
    elif opr == "delete":
        address_id = params['data']['id']
        re_bool, result = AccountService.address_del_api(address_id=address_id)
        return get_ret(result)
    else:
        return build_ret(success=True, msg="该接口还未开放！", code=404)


@route("/admin/address/operation", api="后台地址管理", methods=['GET', 'POST'])
def admin_address():
    params = get_params()
    opr = params['opr']
    if opr == "search":
        data = params['data']
        page = data.get('page')
        limit = data.get('limit')
        cond = data.get('cond')
        login_name = cond.get('login_name').strip()
        total, result = AccountService.admin_address_search_api(login_name=login_name, page=page, limit=limit)
        if total is not False:
            return build_ret(success=True, total=total, data=result)
        else:
            return get_ret(result)
    else:
        return build_ret(success=True, msg="该接口还未开放！", code=404)