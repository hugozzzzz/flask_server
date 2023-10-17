#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json
import sys
# flask
from flask import render_template, redirect, request
from flask import jsonify
# 引入module.py\__init_.py
from app.product import product
from .module import *
# 封装工具
from app.utils import ResponseReturn
# 日志
from app.log import getLogger

logger = getLogger(__name__)


@product.route('/')
def index():
    return "product page"


@product.route('/add')
def add_product():
    try:
        if request.method == 'GET':
            name = request.args.get('name')
        logger.info('success')
        return jsonify(ResponseReturn('', 'result', add_product_fun(name)).getReturnData())
    except Exception as e:
        logger.error("发生异常：{0}".format(e))
        return jsonify(ResponseReturn('', 'result', False).getReturnData())
