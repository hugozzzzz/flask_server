from sqlalchemy import create_engine
from .base import TabBase, sessionmaker
from .bs_product import bs_product
from .bs_user import bs_user
from .bs_dict import bs_dict


def init_dc(connect_str: str, drop_first: bool) -> sessionmaker:
    kwargs = {}
    if not connect_str.startswith(''):
        kwargs.update({'max_overflow': 0,  # 超过连接池大小外最多创建的连接
                       'pool_size': 5,  # 连接池大小
                       'pool_timeout': 30,  # 池中没有线程最多等待的时间，否则报错
                       'pool_recycle': -1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
                       })
    engine = create_engine(connect_str, *kwargs)
    if drop_first:
        TabBase.metadata.drop_all(engine)

    TabBase.metadata.create_all(engine)  # 找到所有继承了Base的类，按照其结构建表
    return sessionmaker(bind=engine)


def get_db_session(connect_str: str) -> sessionmaker:
    """创建数据库表"""
    kwargs = {}
    if not connect_str.startswith(''):
        kwargs.update({'max_overflow': 0,  # 超过连接池大小外最多创建的连接
                       'pool_size': 5,  # 连接池大小
                       'pool_timeout': 30,  # 池中没有线程最多等待的时间，否则报错
                       'pool_recycle': -1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
                       })
    engine = create_engine(connect_str, *kwargs)

    # TabBase.metadata.create_all(engine) #找到所有继承了Base的类，按照其结构建表

    return sessionmaker(bind=engine)
