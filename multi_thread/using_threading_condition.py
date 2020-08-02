#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2020/8/1 19:54
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @File    : using_threading_condition.py
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
# 首先 acquire 一个条件变量，然后判断一些条件
# 如果条件不满足则 wait
# 如果满足条件，进行逻辑处理后，通过 notify 方法通知其他线程，
#    其他处于 wait 中的线程接到通知后会重新判断条件

# 演变出来的条件变量经典问题，是生产者和消费者的问题
import random
import threading
import time

count = 1

con = threading.Condition()


class Producer(threading.Thread):
    def run(self) -> None:
        global count

        while True:
            # 防止线程安全问题，先判断是否拿到锁
            if con.acquire():
                if count > 1000:
                    con.wait()

                # 否则新增商品，保证消费量充足
                count += 100
                print(f'\n{self.name} 新增 100 的商品，当前总数为 {count}')
                con.notify()

                # 释放锁，并等待 1s
                con.release()
                time.sleep(1)


class Consumer(threading.Thread):
    def run(self) -> None:
        global count

        while True:
            if con.acquire():

                if count < 50:
                    con.wait()

                count -= random.randint(30, 70)
                print(f'{self.name} 消费 50 个商品，当前总数为 {count}')
                con.notify()
                con.release()
                time.sleep(.3)


p = Producer()
c = Consumer()
p.start()
c.start()
