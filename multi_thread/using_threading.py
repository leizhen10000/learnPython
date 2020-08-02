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
        print(f'{thread_name}: {time.ctime(time.time())},'
              f' counter: {counter}')
        counter -= 1


class MyThread(threading.Thread):
    # 继承父类 threading.Thread
    def __init__(self, thread_id, name, delay, counter):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.counter = counter
        self.delay = delay

    def run(self):
        print('开始线程：', self.name)
        print_time(threading.current_thread().name, self.delay, 5)
        print('退出线程：', self.name)


print("主线程：", threading.current_thread().name)
# 创建新线程
thread1 = MyThread(1, 'Thread-10', 1, 5)
thread2 = MyThread(2, 'Thread-20', 2, 5)

# 开启线程
# thread2 开启守护进程，在主线程执行完成后，该子线程也会立马结束
thread2.daemon = True
thread1.daemon = True
thread1.start()
thread2.start()

# 设置 thread1 阻塞，会一直等待该线程的结束，设置超时时间
# 3s 后主线程会直接结束，留下 thread1 继续执行
thread1.join(timeout=3)
print('退出主线程')
