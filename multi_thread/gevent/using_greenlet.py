#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2020/8/2 11:14
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @File    : using_greenlet.py
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
import greenlet


def test1():
    print(12)
    gr1.switch()
    print(34)


def test2():
    print(56)
    gr1.switch(gr2)
    print(78)


gr1 = greenlet.greenlet(test1)
gr2 = greenlet.greenlet(test2)
