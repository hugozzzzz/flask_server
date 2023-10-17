#!/usr/bin/python3
# -*- coding: utf-8 -*-
from flask import Blueprint

product = Blueprint('product', __name__)
from app.product import views
