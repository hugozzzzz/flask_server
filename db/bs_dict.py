from .base import TabBase, Column, Integer, String, DateTime, Text, UniqueConstraint, Index, datetime
from .base import ForeignKey, relationship, HintObject


class bs_dict(TabBase):
    # 表名字:
    __tablename__ = 'bs_dict'

    # 表结构:
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=True)
    type = Column(String(32), nullable=True)
    value = Column(String(32), nullable=True)
    isdel = Column(String(1), nullable=True)
    sort = Column(Integer, nullable=True)

    def __str__(self, ):
        return f"bs_dict id:{self.id},name:{self.name},value:{self.value},type:{self.type}]"
