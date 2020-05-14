#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@file    :  permutation_list.py
@time    :  20/2/16 14:13
@author  :  leizhen
@contact :  leizhen8080@foxmail.com
@doc     :  对迭代进行排列组合
"""

from itertools import permutations, combinations, combinations_with_replacement

# itertools 模块提供了三个函数
# 便利一个集合中语速的所有可能排列或组合

items = 'abc'

print('1. 排列')
for p in permutations(items):
    print(p)

# 如果想得到指定长度的所有排列
# 可以传递一个可选的长度参数
print('指定排列组合的长度')
for p in permutations(items, 2):
    print(p)

print('2. 组合')
print('对于组合来说，元素的顺序已经不重要了')

for c in combinations(items, 3):
    print(c)

print('组合参数为 2')
for c in combinations(items, 2):
    print(c)

print('3. 允许同一个元素被选取多次')
for c in combinations_with_replacement(items, 3):
    print(c)
