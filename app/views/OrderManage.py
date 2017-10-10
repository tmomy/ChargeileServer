#!/usr/bin/env python
# encoding: utf-8
"""
@author: leason
@time: 2017/8/30 10:52
"""
from flask import request
from app.untils import get_params
from app.framework_api import route, build_ret, get_ret
from app.services.api import OrderServices
from app.untils.context_get import get_user_info
from app.untils.express_list import public_request


"""
admin订单操作
"""


# 查询运单信息
@route("/waybill/list", api="waybill", methods=['GET', 'POST'])
def waybill_list():
    params = get_params()
    state, result = public_request(params)
    return build_ret(success=state, data=result)


# 查询
@route("/admin/order/list", api="order", methods=['GET', 'POST'])
def list_order():
    params = get_params()
    result, total = OrderServices.service_order_list(params)
    return build_ret(success=True, data=result, total=total)


# 订单详情
@route("/admin/order/detail", api="order", methods=['GET', 'POST'])
def detail_order():
    params = get_params()
    result = OrderServices.service_order_detail(params['order_num'])
    if result:
        return build_ret(success=True, data=result, msg='查询成功')
    else:
        return build_ret(success=False, msg='查询失败')


# 修改订单状态
@route("/admin/order/status/modify", api="order", methods=['GET', 'POST'])
def modify_order_status():
    params = get_params()
    result = OrderServices.service_order_modify_status(params)
    msg = ('修改成功！' if result else '修改失败')
    return build_ret(success=result, msg=msg)


# 绑定订单运单号
@route("/admin/order/express/modify", api="order", methods=['GET', 'POST'])
def modify_order_express():
    params = get_params()
    result = OrderServices.service_order_modify_express(params)
    msg = ('绑定成功！' if result else '绑定失败！')
    return build_ret(success=result, msg=msg)


"""
任务模块（废弃）
"""


# 增加
@route("/admin/task/add", api="task", methods=['GET', 'POST'])
def add_task():
    params = get_params()
    result = OrderServices.service_task_add(params)
    msg = ('操作成功！' if result else '操作失败，请检查余额！')
    return build_ret(success=result, msg=msg)


# 查询
@route("/admin/task/list", api="task", methods=['GET', 'POST'])
def list_task():
    params = get_params()
    result, total = OrderServices.service_task_list(params)
    return build_ret(success=True, data=result, total=total)


# 删除
@route("/admin/task/del", api="task", methods=['GET', 'POST'])
def del_task():
    # params = get_params()
    # result = task.task_del()
    result = OrderServices.service_task_del()
    return build_ret(success=result)


"""
创建订单模块
"""


# 自动生成订单
@route("/admin/order/create", type=True, api="task", methods=['GET', 'POST'])
def create_order():
    params = get_params()
    ip = request.remote_addr
    if ip != '127.0.0.1':
        return build_ret(success=False, msg='禁止访问！')
    if params['key'] != 'c6a3aee2eda0ccb14abb160dcd62c26b':
        return build_ret(success=False, msg='认证失败！')
    result, data = OrderServices.service_create_order()
    msg = ('操作成功！' if result is True else result)
    return build_ret(success=(result==True), msg=msg, data=data)


"""
app端订单模块
"""


# 生成订单的开关
@route("/app/order/switch", api="order", methods=['GET', 'POST'])
def app_order_switch():
    params = get_params()
    params['login_name'] = get_user_info()['username']
    state, result = OrderServices.service_order_switch(params)
    if state:
        return build_ret(success=state, msg='操作成功')
    else:
        return get_ret(result)


# 订单详情
@route("/app/order/detail", api="order", methods=['GET', 'POST'])
def app_detail_order():
    params = get_params()
    result = OrderServices.service_order_detail(params['order_num'])
    msg = ('查询成功！' if result else '查询失败！请输入正确的订单号！')
    return build_ret(success=True, data=result, msg=msg)


# 修改订单状态  -- 完成订单
@route("/app/order/status/modify", api="order", methods=['GET', 'POST'])
def app_modify_order_status():
    params = get_params()
    # 用户只有已收货，拒收货的权限
    if params['order_status'] in [2, 3]:
        result = OrderServices.service_order_modify_status(params)
    else:
        result = False
    msg = ('修改成功！' if result else '修改失败')
    return build_ret(success=result, msg=msg)


# 查询
@route("/app/order/list", api="order", methods=['GET', 'POST'])
def app_list_order():
    params = get_params()
    params['cond']['login_name'] = get_user_info()['username']
    result, total = OrderServices.service_order_list(params)
    return build_ret(success=True, data=result, total=total)


# app查询余额明细
@route("/app/balance/list", api="order", methods=['GET', 'POST'])
def app_list_balance():
    params = get_params()
    params['cond']['login_name'] = get_user_info()['username']
    result, total = OrderServices.service_balance_list(params)
    return build_ret(success=True, data=result, total=total)


# app查询操作记录
@route("/app/operate/list", api="order", methods=['GET', 'POST'])
def app_list_operate():
    params = get_params()
    params['user_id'] = get_user_info()['user_id']
    result, total = OrderServices.service_operate_list(params)
    return build_ret(success=True, data=result, total=total)