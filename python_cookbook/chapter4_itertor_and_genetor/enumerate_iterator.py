#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@file    :  enumerate_iterator.py
@time    :  20/2/16 16:50
@author  :  leizhen
@contact :  leizhen8080@foxmail.com
@desc    :  给迭代添加索引
"""
from collections import defaultdict
from pprint import pprint

my_list = 'bac'

print('迭代索引')
for idx, val in enumerate(my_list):
    print(idx, val)

print('从 1 开始编号')
for idx, val in enumerate(my_list, 1):
    print(idx, val)

print('使用场景：在遍历文件时，需要使用行号定位错误信息所在位置')


def parse_data(filename):
    with open(filename, 'rt') as f:
        for line_no, line in enumerate(f, 1):
            fields = line.split()
            try:
                count = str(fields[1])
            except ValueError as e:
                print(f'Line {line_no}: Parse error: {e}')
            except IndexError as e:
                print(f"Line {line_no}: only has one word : {line}")


parse_data('test.txt')

print('使用场景二：某个单词出现的行，相当于查找关键词频率')

word_summary = defaultdict(list)

with open('test.txt', 'rt') as f:
    lines = f.readlines()

for idx, line in enumerate(lines):
    words = [w.strip().lower() for w in line.split()]
    for word in words:
        word_summary[word].append(idx)

pprint(word_summary)
