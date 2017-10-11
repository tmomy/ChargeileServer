#!/usr/bin/env python
# encoding: utf-8
"""
@author: WL
@time: 2017/10/11 16:58
"""
from lib.utils import package_import
from app.services.untils import ModelBase
from app.db.db_api import Engine
from app.conf import msg

package_import("app.Tables")


def create_all_table():
    ModelBase.metadata.create_all(bind=Engine)
    return True, msg.SUCCESS


def drop_all_table():
    ModelBase.metadata.drop_all(bind=Engine)
    return True, msg.SUCCESS
