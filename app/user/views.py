#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json
import sys
# flask
from flask import render_template, redirect, request
from flask import jsonify
# 引入module.py\__init_.py
from app.user import user
from .module import *
# 封装工具
from app.utils import ResponseReturn
# 日志
from app.log import getLogger

logger = getLogger(__name__)


@user.route('/')
def index():
    return "user page"


@user.route('/addUser')
def add_user():
    try:
        if request.method == 'GET':
            name = request.args.get('name') if request.args.get('name') is not None else ''
            cardId = request.args.get('cardId') if request.args.get('cardId') is not None else ''
            password = request.args.get('password') if request.args.get('password') is not None else ''
            role = request.args.get('role') if request.args.get('role') is not None else ''
        else:
            pass
        return jsonify(ResponseReturn('新增用户成功', 'result', add_user_fun(name, cardId, password, role)).getReturnData())
    except Exception as e:
        logger.error("发生异常：{0}".format(e))
        return jsonify(ResponseReturn('新增用户失败', 'result', False).getReturnData())


# 获取用户列表
@user.route('/getUserList')
def get_user_list():
    try:
        if request.method == 'GET':
            pageSize = int(request.args.get('pageSize')) if request.args.get('pageSize') is not None else 20
            pageIndex = int(request.args.get('pageIndex')) if request.args.get('pageIndex') is not None else 1
        return jsonify(ResponseReturn('', 'result', get_user_list_fun(pageSize,pageIndex)).getReturnData())
    except Exception as e:
        logger.error("发生异常：{0}".format(e))
        return jsonify(ResponseReturn('', 'result', False).getReturnData())


@user.route('/getDict')
def get_dict():
    try:
        if request.method == 'GET':
            type = request.args.get('type') if request.args.get('type') is not None else -1
        else:
            pass
        return jsonify(ResponseReturn('', 'result', get_dict_fun(type)).getReturnData())
    except Exception as e:
        logger.error("发生异常：{0}".format(e))
        return jsonify(ResponseReturn('', 'result', False).getReturnData())