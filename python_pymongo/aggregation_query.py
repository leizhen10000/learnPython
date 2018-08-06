#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/6/1 19:41
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @File    : aggregation_query.py
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

from bson import SON, Code
from pymongo import MongoClient

db = MongoClient().aggregation_eample
# result = db.things.insert_many([
#     {"x": 1, "tags": ["dog", "cat"]},
#     {"x": 2, "tags": ["cat"]},
#     {"x": 2, "tags": ["mouse", "cat", "dog"]},
#     {"x": 3, "tags": []}
# ])
# print(result.inserted_ids)
print(db.collection_names(include_system_collections=False))

pipeline = [
    {"$unwind": "$tags"},
    {"$group": {"_id": "$tags", "count": {"$sum": 1}}},
    {"$sort": SON([("count", -1), ("_id", -1)])}
]
pprint.pprint(list(db.things.aggregate(pipeline)))

# 解释代码内容
result = db.command('aggregate', 'things', pipeline=pipeline, explain=True)
pprint.pprint(result)

mapper = Code("""
function(){
  this.tags.forEach(function(z){
    emit(z, 1);
  });
}
""")
reducer = Code("""
  function (key, values) {
    var total = 0;
    for (var i = 0; i < values.length; i++){
      total += values[i];
    }
    return total;
  }
""")
result = db.things.map_reduce(mapper, reducer, "myresults")
for doc in result.find():
    pprint.pprint(doc)
pprint.pprint(db.things.map_reduce(mapper, reducer, "myresults", full_response=True))
pprint.pprint(db.things.map_reduce(
    mapper, reducer,
    out=SON([("replace", "results"), ("db", "outdb")]),
    full_response=True))
