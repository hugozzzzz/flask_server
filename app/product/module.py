#!/usr/bin/python3
# -*- coding: utf-8 -*-

# flask
from flask import g, render_template, redirect, request
from sqlalchemy.sql import func
# 数据表导入
from db import bs_product
# 日志
from app.log import getLogger

logger = getLogger(__name__)


def add_product_fun(name):
    g.db.add(bs_product(name=name))
    g.db.commit()
    return True
