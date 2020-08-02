#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2020/8/1 08:51
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @File    : using_coroutine.py
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


# 协程不被操作系统内核管理，而是由程序完全控制
# 不需要多线程的锁机制，只有一个线程不存在变量冲突
# 对于多核 CPU，利用多线程+协程的方式，能充分利用 CPU，获得极高的性能

# yield 相当于暂停功能，程序运行到 yield 停止
# send 可以传参给生成器函数，参数赋值给 yield
def customer():
    while True:
        number = yield
        print("开始消费", number)


c = customer()
next(c)
for i in range(4):
    print('开始生产', i)
    c.send(i)
