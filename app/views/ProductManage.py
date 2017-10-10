#!/usr/bin/env python
# encoding: utf-8
"""
@author: XX
@time: 2017/9/5 10:54
"""
from app.untils import get_params
from app.framework_api import route, build_ret, get_ret
from app.services.api import ProductService


@route("/spu", api="spu", methods=['GET', 'POST'])
def category():
    params = get_params()
    opr = params['opr']
    if opr == "search":
        data, total = ProductService.service_spu_search(params=params['data'])
        return build_ret(success=True, data=data, total=total)
    elif opr == "modify":
        resp, msg = ProductService.service_spu_edit(params=params['data'])
        return get_ret(error=msg)
    elif opr == "delete":
        resp, msg = ProductService.service_spu_delete(params=params["data"])
        return get_ret(error=msg)
    elif opr == "add":
        ProductService.service_spu_add(params=params["data"])
        return build_ret(success=True, msg="添加成功")


@route("/spu/attr", api="spu/attr", methods=['GET', 'POST'])
def category():
    params = get_params()
    opr = params['opr']
    if opr == "delete":
        resp, msg = ProductService.service_spu_attr_delete(params=params['data'])
        return get_ret(error=msg)


@route("/sku", api="sku", methods=['GET', 'POST'])
def category():
    params = get_params()
    opr = params['opr']
    if opr == "search":
        data, total = ProductService.service_sku_search(params=params['data'])
        return build_ret(success=True, data=data, total=total)
    elif opr == "modify":
        resp, msg = ProductService.service_sku_edit(params=params["data"])
        return get_ret(error=msg)
    elif opr == "add":
        resp, msg = ProductService.service_sku_add(params=params["data"])
        return get_ret(error=msg)
    elif opr == "delete":
        resp, msg = ProductService.service_sku_delete(params=params["data"])
        return get_ret(error=msg)


@route("/sku/attr", api="sku/attr", methods=['GET', 'POST'])
def category():
    params = get_params()
    opr = params['opr']
    if opr == "search":
        result = ProductService.service_product_attr_get(spu_id=params["data"]["spu_id"])
        return build_ret(success=True, data=result, msg="查询成功")
    elif opr == "delete":
        resp, msg = ProductService.service_sku_attr_delete(params=params["data"])
        return get_ret(error=msg)


@route("/product/info", api="/product/info", methods=['GET', 'POST'])
def category():
    params = get_params()
    opr = params['opr']
    if opr == "search":
        result, total = ProductService.service_product_search(params=params["data"])
        return build_ret(success=True, data=result, msg="查询成功", total=total)
    elif opr == "add":
        resp, msg = ProductService.service_product_add(params=params["data"])
        return get_ret(error=msg)
    elif opr == "modify":
        resp, msg = ProductService.service_product_edit(params=params["data"])
        return get_ret(error=msg)
    elif opr == "delete":
        resp, msg = ProductService.service_product_delete(params=params["data"])
        return get_ret(error=msg)


@route("/product/tree", api="/product/tree", methods=['GET', 'POST'])
def category():
    params = get_params()
    opr = params['opr']
    if opr == "search":
        result = ProductService.service_product_tree_search()
        return build_ret(success=True, data=result, msg="查询成功")


@route("/product/recommend", api="/product/recommend", methods=['GET', 'POST'])
def recommend_prodcut():
    params = get_params()
    opr = params['opr']
    if opr == "search":
        result, total = ProductService.service_product_recommend(params=params["data"])
        return build_ret(success=True, data=result, msg="查询成功", total=total)