#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time    : 2023/1/8 19:21
# @Author  : paulinelee
# @Site    : https://github.com/llaichiyu/
# @File    : book.py
# @Software: PyCharm


from sqlalchemy import Column, Integer, String
from flask_sqlalchemy import SQLAlchemy
# from app.models import app

# db = SQLAlchemy(app=app, engine_options=app.config['SQLALCHEMY_DATABASE_URI'])
db = SQLAlchemy()


class Book(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    author = Column(String(30), default='未名')
    binding = Column(String(20))
    publisher = Column(String(50))
    price = Column(String(20))
    pages = Column(Integer)
    pubdate = Column(String(20))
    isbn = Column(String(15), nullable=False, unique=True)
    summary = Column(String(1000))
    image = Column(String(50))
