#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2020/5/14 14:03
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @File    : using_threading_event.py
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

# 实现线程间的通信

# 使一个线程等待其他线程的通知

# 内置标志，初始值为 False
import time

event = threading.Event()


def func():
    # 等待事件，进入阻塞状态
    print(threading.current_thread().name, 'wait for event ...')
    event.wait()
    # 收到事件后进入运行状态
    print(threading.current_thread().name, 'recv event.')


if __name__ == '__main__':
    t1 = threading.Thread(target=func)
    t2 = threading.Thread(target=func)
    t1.start()
    t2.start()

    time.sleep(2)

    # 发送事件通知，设置内置标示为 True
    print('MainThread set event.')
    event.set()
