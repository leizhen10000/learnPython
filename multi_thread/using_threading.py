#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/4/8 14:27
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @File    : using_threading.py
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
import threading

exit_flag = 0

class MyThread(threading.Thread):
    # 继承父类 threading.Thread
    def __init__(self):
        threading.Thread.__init__(self)
        self.