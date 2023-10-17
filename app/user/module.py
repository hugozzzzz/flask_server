#!/usr/bin/python3
# -*- coding: utf-8 -*-

# flask
from flask import g, render_template, redirect, request
from sqlalchemy.sql import func
# 数据表导入
from db import bs_user, bs_dict
# 日志
from app.log import getLogger
import datetime

logger = getLogger(__name__)


def get_dict_fun(type):
    info = g.db.query(bs_dict).filter(bs_dict.type == type).all()
    res = []
    for i in info:
        obj = {'name': i.name, 'value': i.value}
        res.append(obj)
    return res


def add_user_fun(name, cardId, password, role):
    g.db.add(bs_user(name=name, cardId=cardId, password=password, role=role))
    g.db.commit()
    return True


def get_user_list_fun(pageSize, pageIndex):
    total = g.db.query(bs_user).count()
    info = g.db.query(bs_user).offset((pageIndex - 1) * pageSize).limit(pageSize)
    res = []
    for i in info:
        obj = {'id': i.id, 'name': i.name, 'cardId': i.cardId, 'role': i.role,
               'create_date': i.create_date.strftime('%Y-%m-%d %H:%M:%S') if i.create_date != None else ''}
        res.append(obj)
    result = {'total': total, 'info': res}
    return result
