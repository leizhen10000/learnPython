#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/31 08:14
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @File    : __init__.py.py
# @Software: PyCharm
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
             ┏┓   ┏┓
            ┏┛┻━━━┛┻┓
            ┃  ☃    ┃
            ┃ ┳┛  ┗┳ ┃
            ┃      ┻  ┃
            ┗━┓     ┏━┛
              ┃     ┗━━━┓
              ┃ 神兽保佑 ┣┓
              ┃ 永无BUG┏┛
              ┗┓┓┏━┳┓┏┛
               ┃┫┫ ┃┫┫
               ┗┻┛ ┗┻┛
"""
import pprint
import pymongo
from datetime import datetime

from bson import ObjectId
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
# client = MongoClient('mongodb://localhost:27017/')
db = client.anjuke
# db = client['anjuke']
collection = db.anjuke

print(db)
print(collection)

post = [
    {"author": "Mike",
     "text": "My first blog post!",
     "tags": ["mongodb", "python", "pymongo"],
     "date": datetime.now()
     },
    {"author": "Eliot",
     "text": "MongoDB is fun",
     "tags": ["mongodb", "python", "pymongo"],
     "date": datetime.now()
     },
]

posts = db.posts
# post = posts.insert_one(post).inserted_id
# post_ids = posts.insert_many(post).inserted_ids
# print(post_ids)

print(db.collection_names(include_system_collections=False))

pprint.pprint(posts.find_one())

pprint.pprint(posts.find_one({"author": "Mike"}))

pprint.pprint(posts.find_one({"_id": ObjectId('5b0ff53225c0f4ad30b85951')}))

print('=' * 20)
for post in posts.find():
    pprint.pprint(post)

print('=' * 30)
print(posts.count())
print(posts.find({"author": "Mike"}).count())

print('=' * 30)
d = datetime(2010, 11, 12, 12, 23, 45)
for post in posts.find({"date": {"$gt": d}}).sort("author"):
    pprint.pprint(post)

print('=' * 30)
result = db.posts.create_index([('user_id', pymongo.ASCENDING)],
                               unique=True)
sorted(list(db.posts.index_information()))
