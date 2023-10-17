#!/usr/bin/python3
# -*- coding: utf-8 -*-

from app import app, set_db_path, connect_db, socketio
from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView
from db import get_db_session, sessionmaker, bs_product

if __name__ == '__main__':
    USERNAME = 'root'
    PASSWORD = '12345678'
    HOST = '192.168.2.102'
    PORT = '3306'
    DATABASE = 'mine'
    db_url = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOST, PORT, DATABASE)
    set_db_path(db_url)
    admin = Admin(app)


    class MyView(BaseView):  # 这里类似于app.route()，处理url请求
        @expose('/')
        def index(self):
            return self.render('index.html')


    admin.add_view(MyView(name=u'Hello'))
    admin.add_view(ModelView(bs_product, connect_db()))

    app.run(host='192.168.2.102', port='8082', debug=False)
    # socketio.run(app, host='192.168.2.102', port=8082, debug=False)
