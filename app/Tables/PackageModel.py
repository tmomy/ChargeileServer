#!/usr/bin/env python
# encoding: utf-8
"""
@author: XX
@time: 2017/9/4 14:17
"""
import time
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import Date
from sqlalchemy import Text

from app.framework_api import date_time
from app.services.untils import ModelBase


class Package(ModelBase):
    __tablename__ = "package"
    __table_args__ = {
        'mysql_auto_increment': '10001'
    }

    package_id = Column(Integer, primary_key=True, autoincrement=True)
    package_name = Column(String(length=100), nullable=False)
    status = Column(Integer, nullable=False)
    create_time = Column(String(length=100))
    effect_time = Column(String(length=100))
    description = Column(Text)
    detail = Column(Text)
    thumbnail = Column(Text)

    def __init__(self, package_name, status, effect_time, description, detail, thumbnail):
        self.package_name = package_name
        self.status = status
        self.create_time = date_time()
        self.effect_time = effect_time
        self.description = description
        self.detail = detail
        self.thumbnail = thumbnail

    def to_json(self):
        return {
            'package_id': self.package_id,
            'package_name': self.package_name,
            'status': self.status,
            'create_time': self.create_time,
            'effect_time': self.effect_time,
            'description': self.description,
            'detail': self.detail,
            'thumbnail': self.thumbnail
        }

    def __repr__(self):
        return "<package_id={},package_name={},status={},create_time={},effect_time={},description={}," \
               "detail={},thumbnail={}>".format(
            self.package_id, self.package_name, self.status, self.create_time,self.effect_time,
            self.description, self.detail, self.thumbnail)


class PackageMapProduct(ModelBase):
    __tablename__ = "package_map_product"
    __table_args__ = {
        'mysql_auto_increment': '10001'
    }

    id = Column(Integer, primary_key=True, autoincrement=True)
    package_id = Column(Integer, ForeignKey('package.package_id', ondelete='CASCADE'))
    product_id = Column(Integer, ForeignKey('product.product_id', ondelete='CASCADE'))

    def __init__(self, package_id, product_id):
        self.package_id = package_id
        self.product_id = product_id

    def to_json(self):
        return {
            'id': self.id,
            'attr_id': self.package_id,
            'product_id': self.product_id
        }

    def __repr__(self):
        return "<id={},package_id={},product_id={}>".format(self.id, self.package_id, self.product_id)
