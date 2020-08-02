#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2020/5/14 14:25
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @File    : using_threading_local.py
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

local_school = threading.local()


def process_student():
    std = local_school.student
    print(f"Hello, {std} in {threading.current_thread().name}")


def process_thread(name):
    local_school.student = name
    process_student()


if __name__ == '__main__':
    t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
    t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    a = [1, 12, 9, 8]
    print(sorted(list(tuple(a)), reverse=True))
    a.reverse()

    new_a = []
    for i in a:
        if i not in new_a:
            new_a.append(i)
    print(sorted(new_a, reverse=True))
    print(new_a.reverse())

    import time


    def consumer():
        while True:
            x = yield


    def producer():
        g = consumer()
        next(g)
        for i in range(1000000):
            g.send(i)


    start = time.time()

    producer()
    print(time.time() - start)
