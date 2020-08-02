#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2020/8/2 10:06
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @File    : using_threading_timer.py
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
import time


def func(num):
    print(f'hello {num} timer!')


timer = threading.Timer(1.5, func, (1,))
time_0 = time.time()
timer.start()
timer.join()
print(time.time() - time_0)

timer2 = threading.Timer(3, func, (2,))
timer2.start()
time.sleep(2)
if timer2.is_alive():
    # 如果 2s 后还存活，则取消 timer2 的执行
    timer2.cancel()

print(timer.is_alive())
print(timer2.is_alive())