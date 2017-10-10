#!/usr/bin/env python
# encoding: utf-8
"""
@author: WL
@time: 2017/8/25 17:33
"""


# 更新字段值
def field_update(table, field, value=1):
    if not hasattr(table, field):
        return False
    setattr(table,field,value)
    return table

