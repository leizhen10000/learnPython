#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/10 22:00
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @File    : prime_demo.py
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
from itertools import islice


def prime(n):
    """
    这个方法非常的蠢，数据量100000还能跑，
    数据量 1000,000 直接就炸了
    :param n:
    :return:
    """
    if n <= 1:
        return 0
    for i in range(2, n + 1):
        if n % i == 0:
            return 0
    return 1


# 生成器，不断返回下一个素数
# 推荐使用生成器
#
def primes(num):
    num_list = range(2, int(num) + 1)
    while True:
        n = next(iter(num_list))
        yield n
        num_list = filter(lambda x: (x % n > 0), num_list)  # 构造新序列
        # for aa in num_list:
        #     print(aa)


if __name__ == '__main__':
    # for i in range(2, 10000):
    #     if prime(i):
    #         print(i) # 0.72s
    # primes(10000) # 0.08s
    for item in islice(primes(1000), 100):
        print(item)  # 耗费的时间2.63s
