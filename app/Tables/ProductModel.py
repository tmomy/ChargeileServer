#!/usr/bin/env python
# encoding: utf-8
"""
@author: XX
@time: 2017/8/30 14:15
"""
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Text
from sqlalchemy.orm import relationship
from app.services.untils import ModelBase
from app.framework_api import date_time


class SPU(ModelBase):
    __tablename__ = "spu"
    __table_args__ = {
        'mysql_auto_increment': '10001'
    }

    spu_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=50))
    create_time = Column(String(length=50))
    category_id = Column(Integer, ForeignKey('category.category_id', ondelete='CASCADE'))

    def __init__(self, name, category_id):
        self.name = name
        self.create_time = date_time()
        self.category_id = category_id

    def to_json(self):
        return {
            'spu_id': self.spu_id,
            'name': self.name,
            'category_id': self.category_id,
            'create_time': self.create_time
        }

    def __repr__(self):
        return "<spu_id={},name={},category_id={},create_time={}>".format(self.spu_id,
             self.name, self.category_id, self.create_time)


class SKU(ModelBase):
    __tablename__ = "sku"
    __table_args__ = {
        'mysql_auto_increment': '10001'
    }

    sku_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=50))
    spu_id = Column(Integer, ForeignKey('spu.spu_id', ondelete='CASCADE'))
    slogan = Column(String(length=200))
    origin = Column(String(length=50))
    seller_id = Column(String(length=50))
    create_time = Column(String(length=50))

    children = relationship("SKUMapAttr")

    def __init__(self, spu_id, name, slogan, origin, seller_id):
        self.spu_id = spu_id
        self.name = name
        self.slogan = slogan
        self.seller_id = seller_id
        self.origin = origin
        self.create_time = date_time()

    def to_json(self):
        return {
            'sku_id': self.sku_id,
            'name': self.name,
            'spu_id': self.spu_id,
            'origin': self.origin,
            'seller_id': self.seller_id,
            'slogan': self.slogan,
            'create_time': self.create_time
        }

    def __repr__(self):
        return "<sku_id={},name={},spu_id={},origin={},slogan={},seller_id={},create_time={}>".\
            format(self.sku_id, self.name, self.spu_id, self.origin, self.slogan, self.seller_id, self.create_time)


class SKUMapAttr(ModelBase):
    __tablename__ = "sku_map_attr"
    __table_args__ = {
        'mysql_auto_increment': '10001'
    }

    id = Column(Integer, primary_key=True, autoincrement=True)
    sku_id = Column(Integer, ForeignKey('sku.sku_id', ondelete='CASCADE'))
    attr_info_id = Column(Integer, ForeignKey('attr_info.id', ondelete='CASCADE'))

    def __init__(self, sku_id, attr_info_id):
        self.sku_id = sku_id
        self.attr_info_id = attr_info_id

    def to_json(self):
        return {
            'id': self.id,
            'sku_id': self.sku_id,
            'attr_info_id': self.attr_info_id
        }

    def __repr__(self):
        return "<id={},sku_id={},attr_info_id={}>".format(self.id, self.sku_id, self.attr_info_id)


class Product(ModelBase):
    __tablename__ = "product"
    __table_args__ = {
        'mysql_auto_increment': '10001'
    }

    product_id = Column(Integer, primary_key=True, autoincrement=True)
    sku_id = Column(Integer, ForeignKey('sku.sku_id', ondelete='CASCADE'))
    spu_id = Column(Integer)
    category_id = Column(Integer)
    price = Column(Integer)
    discount = Column(Integer)
    storage = Column(Integer)
    attr_str = Column(String(255))
    pic_url = Column(Text)
    create_time = Column(String(length=50))

    def __init__(self, sku_id, spu_id, category_id, price, discount, storage, attr_str, pic_url):
        self.sku_id = sku_id
        self.spu_id = spu_id
        self.category_id = category_id
        self.price = price
        self.discount = discount
        self.attr_str = attr_str
        self.storage = storage
        self.pic_url = pic_url
        self.create_time = date_time()

    def to_json(self):
        return {
            'product_id': self.product_id,
            'sku_id': self.sku_id,
            'spu_id': self.spu_id,
            'category_id': self.category_id,
            'price': self.price,
            'storage': self.storage,
            'attr_str': self.attr_str,
            'pic_url': self.pic_url,
            'create_time': self.create_time
        }

    def __repr__(self):
        return "<product_id={},sku_id={},spu_id={},category_id={},price={},discount={},storage={},attr_str={}," \
               "pic_url={},create_time={}>".format(self.product_id, self.sku_id, self.spu_id, self.category_id,
                                                   self.price, self.discount, self.storage, self.attr_str, self.pic_url,
                                                   self.create_time)




