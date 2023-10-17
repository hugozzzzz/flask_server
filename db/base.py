from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Text, ForeignKey, DateTime
from sqlalchemy import Column,UniqueConstraint, Index,ForeignKey
from sqlalchemy.orm import relationship,sessionmaker

TabBase = declarative_base()


class HintObject(object):
    pass