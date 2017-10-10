#!/usr/bin/env python
# encoding: utf-8
"""
@author: WL
@time: 2017/8/28 14:32
"""
from flask import g, request


def get_params():
    params = getattr(request, "params")
    return params


def get_user_info():
    """
    
    :return: 
    {
        'username': str(username),
        'user_id': str(user_id),
        'type': str(role_type),
        'role_name': role_name,
        'iat': iat,
        'exp': exp
    }
    """
    user_info = getattr(g, "user_info")
    return user_info


def get_rule_set():
    rule_set = getattr(g, "rule_set")
    if rule_set is None:
        rule_set = []
    return rule_set

