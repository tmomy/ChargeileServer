#!/usr/bin/env python
# encoding: utf-8
"""
@author: XX
@time: 2017/9/12 14:29
"""
from app.untils import get_params
from app.framework_api import route, build_ret, get_ret
from app.services.api import ProductService


@route("/package", api="package", methods=['GET', 'POST'])
def category():
    params = get_params()
    opr = params['opr']
    if opr == "search":
        data, total = ProductService.service_package_search(params=params['data'])
        return build_ret(success=True, data=data, total=total)
    elif opr == "add":
        resp, msg = ProductService.service_package_add(params=params['data'])
        return get_ret(error=msg)
    elif opr == "modify":
        resp, msg = ProductService.service_package_edit(params=params['data'])
        return get_ret(error=msg)
    elif opr == "delete":
        resp, msg = ProductService.service_package_delete(params=params['data'])
        return get_ret(error=msg)


@route("/package/product", api="package/product", methods=['GET', 'POST'])
def category():
    params = get_params()
    opr = params['opr']
    if opr == "delete":
        resp, msg = ProductService.service_package_product_delete(params=params['data'])
        return get_ret(error=msg)
