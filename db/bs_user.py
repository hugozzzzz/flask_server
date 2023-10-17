from .base import TabBase, Column, Integer, String, DateTime, Text, UniqueConstraint, Index, datetime
from .base import ForeignKey, relationship, HintObject


class bs_user(TabBase):
    # 表名字:
    __tablename__ = 'bs_user'

    # 表结构:
    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=True)
    cardId = Column(Integer, nullable=True)
    password = Column(String(64), nullable=True)
    status = Column(String(32), nullable=True)
    role = Column(String(32), default='1')
    create_date = Column(DateTime, default=datetime.now)

    def __str__(self, ):
        return f"bs_user id:{self.id},name:{self.name},cardId:{self.cardId},password:{self.password}"
