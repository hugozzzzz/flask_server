from flask import Flask, request, render_template, abort, g
from app.product import product
from app.user import user
import json
from db import get_db_session, sessionmaker, bs_product
from flask_socketio import SocketIO, emit, disconnect, join_room, leave_room

app = Flask(__name__)
'''
app.config['SECRET_KEY'] = True
app.config.from_pyfile("python文件名称")  # 配置文件调用
app.config.from_envvar("环境变量名称", silent=True)  # 环境变量的值为python文件名称名称，内部调用from_pyfile方法
app.config.from_json("json文件名称")  # JSON文件名称，必须是json格式，因为内部会执行json.loads
app.config.from_mapping({'DEBUG': True})  # 字典格式
app.config.from_object("python类或类的路径")
'''
# 通过blueprint分模块
app.register_blueprint(product, url_prefix='/api/product')
app.register_blueprint(user, url_prefix='/api/user')

# websocket配置,失败！
socketio = SocketIO()
socketio.init_app(app, cors_allowed_origins='*')


@app.route('/push')
def push():
    socketio.emit('/chat', {'data': 'hello websocket'}, namespace='chat')
    return 'done'


@socketio.on('connect', namespace='chat')
def connect():
    print('链接成功')


@socketio.on('disconnect', namespace='chat')
def disconnect():
    print('断开连接')


@app.route('/')
def hi():
    return 'hello'


@app.route('/hello', methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        id = request.args.get('id')
    else:
        data = request.get_data()
        json_data = json.loads(data.decode("utf-8"))
    print(id)
    # abort(404)
    return 'hello'


# @app.errorhandler(404)
# def handle_404_error(err):
#     return render_template('404.html')


# @app.before_first_request
# def before_first_request():
#     print("before_first_request")

# ------------------------数据库操作封装------------------------
@app.before_request
def before_request():
    # print("before_request")
    # 调用接口前打开数据库连接并保存，调用接口过程中使用连接，在每次接口调用结束后再关闭
    g.db = connect_db()


@app.after_request
def after_request(response):
    # print("after_request")
    # 关闭数据库连接
    g.db.close()
    return response


def set_db_path(db_url):
    # 保存数据库连接url
    app.config['DATABASE'] = db_url


def connect_db():
    # 返回数据库连接
    return get_db_session(app.config['DATABASE'])()
