import os

from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base, declared_attr


class BaseClass:
    _id = Column("id", Integer, primary_key=True)

    @declared_attr
    def __tablename__(self):
        return self.__name__.lower()


Base = declarative_base(cls=BaseClass)
