#!/usr/local/anaconda3/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, DateTime

import pymysql
pymysql.install_as_MySQLdb()


engine = create_engine('mysql+mysqldb://root@localhost:3306/shiyanlou?charset=utf8')
Base = declarative_base()

class Repository(Base):
    __tablename__ = 'repositories1'

    id = Column(Integer,primary_key=True)
    name = Column(String(64))
    update_time = Column(DateTime)

if __name__ == '__main__':
    Base.metadata.create_all(engine)