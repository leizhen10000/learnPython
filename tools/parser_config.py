#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
# @Time    : 19/11/20 10:23
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @Site    : http://www.leizhen.com
# @File    : parser_config.py
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
# parser 还没有完善，先用简单的读取方法
import re
from collections import OrderedDict

import pymysql
from DBUtils.PersistentDB import PersistentDB
from DBUtils.PooledDB import PooledDB


def get_config():
    with open('../.env') as f:
        for data in f:
            data.strip()  # 去除两端空格
            key, value = re.match(r'(\S+)=(\S+)', data).groups()
            yield key, value


def get_db_tool(is_multi_thread=False):
    config = OrderedDict(list(get_config()))
    config['port'] = int(config['port'])
    if not is_multi_thread:
        pool_db = PersistentDB(
            creator=pymysql,  # 指定数据库连接驱动
            maxusage=1000,  # 连接最大复用次数
            **config
        )
    else:
        pool_db = PooledDB(
            creator=pymysql, maxconnections=3, mincached=2, maxcached=5,
            maxshared=3, blocking=True, setsession=[], ping=0, **config
        )
    return pool_db

# if __name__ == '__main__':
#     db_pool = get_db_tool()
#     conn = db_pool.connection()
#     cursor = conn.cursor()
#     cursor.execute('INSERT INTO douyin_user (suren_id, total_favourited, dongtai_count) VALUES ("123456", 12, 120)')
#     conn.commit()
#     # cursor.execute('SELECT * FROM douyin_user')
#     # result = cursor.fetchone()
#     # print(result)
#     conn.close()
