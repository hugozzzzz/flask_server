from .base import TabBase, Column, Integer, String, DateTime, Text, UniqueConstraint, Index, datetime
from .base import ForeignKey, relationship, HintObject


class bs_product(TabBase):
    # 表名字:
    __tablename__ = 'bs_product'

    # 表结构:
    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=True)  # index指定是否是索引，nullable是否能为空
    num = Column(Integer, nullable=True)
    status = Column(String(32), nullable=True)  # 状态 0：创建、1：启动、2：终止
    type = Column(String(32), default='1')
    model = Column(String(64), nullable=True)  # 型号
    # 注意，此处设置时datetime.datetime.now若加了括号，则时间永远是程序启动时的时间，后面创建数据时，不会变化
    create_date = Column(DateTime, default=datetime.now)
    create_person = Column(Integer, nullable=True)

    # foreign_keys=绑定外键 多次 relationship 反差会识别不出指定数据所以添加 foreign_keys 参数。
    # bs_product_compt = relationship("bs_product_compt", backref='bs_product')

    def __str__(self, ):
        return f"bs_product id:{self.id},name:{self.name},model:{self.model},protocol:{self.protocol}"
