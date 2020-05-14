#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@file    :  multi_iterator.py
@time    :  20/2/16 17:26
@author  :  leizhen
@contact :  leizhen8080@foxmail.com
@desc    :  同时迭代多个序列
"""
from itertools import zip_longest, chain

print('同时迭代多个序列')

x_pts = [1, 5, 4, 2, 10, 7]
y_pts = [101, 79, 23, 89, 12]

for x, y in zip(x_pts, y_pts):
    print(x, y)

print('如果两个序列长度不一致，默认以较短的长度为基准')

a = [1, 2, 3]
b = 'python'
for i in zip(a, b):
    print(i)

print('强制与较长的长度为基准，较短的缺失值则为 None')

for i in zip_longest(a, b):
    print(i)

print('以上为同时迭代两个对象，且并行操作')
print('下面为对两个对象做相同操作，防止多次循环')

for x in chain(a, b):
    print(x)

print('chain 的效率比 “+” 链接两个序列快很多，而且他不需要两个对象的类型一致')
