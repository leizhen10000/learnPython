#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2020/8/1 08:56
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @File    : using_threading_lock.py
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

# 某些变量，让他们在各自的线程中独立

import threading
import time

num = 0

lock = threading.RLock()


def show(arg):
    lock.acquire()
    global num
    time.sleep(.3)
    num += 1
    print('bb', arg, ' num', num)
    lock.release()


print('主线程', threading.current_thread().name, ' 开始')

for i in range(5):
    t = threading.Thread(target=show, args=(i,))
    t.start()
    t.join()


class WorkThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.t_name = name

    def run(self) -> None:
        global num
        while True:
            lock.acquire()
            print(f'\n{self.t_name} locked, number: {num}')
            if num >= 10:
                lock.release()
                print(f'{self.t_name} released, number: {num}')
                break
            num += 1
            print(f'{self.t_name} released, number: {num}')
            lock.release()


local_manager = threading.local()


def thread_poc():
    lock.acquire()
    try:
        print(f'Thread={local_manager.thread_name}')
        print(f'Name={local_manager.name}')
    finally:
        lock.release()


class MyThread(threading.Thread):
    def __init__(self, thread_name, name):
        super().__init__(name=thread_name)
        self._name = name

    def run(self) -> None:
        global local_manager
        local_manager.thread_name = self.name
        local_manager.name = self._name
        thread_poc()


for i in range(5):
    t = MyThread(f'A-{i}', f'a-{i}')
    t.start()

t1 = WorkThread('A-worker')
t2 = WorkThread('B-worker')
t1.start()
t2.start()

print('主线程', threading.current_thread().name, ' 结束')
