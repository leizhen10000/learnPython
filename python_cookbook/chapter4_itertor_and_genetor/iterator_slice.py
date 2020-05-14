#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@file    :  iterator_slice.py
@time    :  20/2/16 13:01
@author  :  leizhen
@contact :  leizhen8080@foxmail.com
"""

from itertools import islice


# 如果想得到一个由迭代器生成的切片对象，但是标准切片操作并不能做到

def count(n):
    while True:
        yield n
        n += 1


c = count(0)

# print(c[10:20])
# 这里会报错


for x in islice(c, 10, 20):
    print(x)

# 如果明确知道要跳过的元素，可以添加 None 为参数
items = ['a', 'b', 'c', 1, 4, 10, 15]
print('跳过前三行')
for idx, x in enumerate(islice(items, 3, None), 1):
    print(idx, x)
print('只要前三行')
for idx, x in enumerate(islice(items, None, 4), 1):
    print(idx, x)
