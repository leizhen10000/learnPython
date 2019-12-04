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
import time

exit_flag = 0


def print_time(thread_name, delay, counter):
    while counter:
        if exit_flag:
            thread_name.exit()
        time.sleep(delay)
        print(f'{thread_name}: {time.ctime(time.time())}')
        counter -= 1


class MyThread(threading.Thread):
    # 继承父类 threading.Thread
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print('开始线程：', self.name)
        print_time(self.name, self.counter, 5)
        print('退出线程：', self.name)


# 创建新线程
thread1 = MyThread(1, 'Thread-1', 1)
thread2 = MyThread(2, 'Thread-2', 2)

# 开启线程
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print('退出主线程')
