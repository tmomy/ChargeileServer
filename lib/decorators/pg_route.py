# encoding: utf-8

"""
@version: 1.0
@author: dawning
@contact: dawning7670@gmail.com
@time: 2017/3/29 9:28
"""
from lib.flask import app
from app.conf import web


rules = []
login_list = []


# route装饰器
# 处理app.route装饰的方法名称相同的情况
def route(rule, api, role='root', type=0, **options):
    def wrapper(func):
        options['endpoint'] = rule
        # 处理多版本api
        for rl in make_rule(web['url_pre'], web['api_version'], rule):
            if type:
                login_list.append(rl)
            rules.append((role, api, rl))
            app.route(rl, **options)(func)
        return wrapper
    return wrapper


def make_rule(prefix, api_vers, rule):
    if not prefix.endswith("/"):
        prefix += "/"
    return [prefix + api + rule for api in api_vers]


def checklist(opr):
    benchmark = set(web['opr'])
    check_opr = set(opr)
    return check_opr.issubset(benchmark)
