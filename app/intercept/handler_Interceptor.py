#!/usr/bin/env python
# encoding: utf-8
"""
@author: WL
@time: 2017/8/25 9:52
"""
import json
from lib.flask import app
from lib.decorators import rules, login_list
from flask import request,make_response, g
from app.untils.log_builder import build_log
from app.conf.config import log, web
from app.untils.context_get import get_user_info, get_params
from app.conf import msg
from app.framework_api import redis_service, get_ret
from app.services.SystemLoginService.lib import de_token
import threading

_ident = threading._get_ident()


logging = build_log(log_config=log)


@app.before_request
def valid_account():
    token = request.headers.get('authorization')
    if request.path in login_list:
        account_info = de_token(token)
        if account_info is None:
            account_info = {
                "type": 1
            }
    else:
        account_info = de_token(token)
        if account_info is None and request.method != "OPTIONS":
            msgs = msg.ERROR(403, "登录失效，请重新登录！")
            resp = get_ret(msgs)
            return make_response(resp)
    setattr(g, "user_info", account_info)


@app.before_request
def context_handler():
    setattr(g, 'rule_set', rules)


@app.before_request
def route_handler():
    re = request.method
    user_info = get_user_info()
    if user_info is None:
        msgs = msg.ERROR(403, "会话失效！")
        resp = get_ret(msgs)
        return make_response(resp)
    redis_key = web['rule_redis_pix'] + str(user_info['type'])
    rule_dict = redis_service.get(redis_key)
    if rule_dict is None or not web['enable_rule']:
        pass
    else:
        params = get_params()
        if isinstance(params, dict):
            opr = params.get('opr')
        else:
            opr = None
        rule_dicts = json.loads(rule_dict)
        if request.path in login_list:
            pass
        elif not opr:
            for routes in rule_dicts.values():
                if request.path in routes:
                    msgs = msg.ERROR(403, "权限受限！")
                    resp = get_ret(msgs)
                    return make_response(resp)
        else:
            if request.path in rule_dicts[opr]:
                msgs = msg.ERROR(403, "权限受限！")
                resp = get_ret(msgs)
                return make_response(resp)


@app.after_request
def response_handler(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type,authorization'
    response.headers['Access-Control-Expose-Headers'] = "authorization"
    logging.info("response is [{}]".format(response.data))
    return response

