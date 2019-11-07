#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2019/11/7 07:40
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


# 改变对象的字符串显示
## 重新定义 __str__() 和 __repr__()

class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y
