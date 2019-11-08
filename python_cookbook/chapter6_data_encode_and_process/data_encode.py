#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
# @Time    : 19/11/7 16:45
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @Site    : http://www.leizhen.com
# @File    : data_encode.py
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
# 处理不同方式编码的山上，比如 CSV 文件，JSON,XML 和二进制包装记录
import csv
from collections import namedtuple

with open('a.csv') as f:
    f_csv = csv.reader(f)
    headings = next(f_csv)
    Row = namedtuple('Row', headings)
    for r in f_csv:
        row = Row(*r)
        print(row)

print('\n')
print('=' * 20)
print('另一种方法，把数据读取到一个字典序列中去')
with open('a.csv') as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        print(row.items())

print('\n')
print('=' * 20)
print('写入数据')
headers = ['a', 'b', 'c', 'd']
rows = [[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 1, 2, 3]]
with open('b.csv', 'w', newline="") as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(rows)

print('如果有字典序列的数据，可以这样写入')
rows = [
    {'a': 1, 'b': 2, 'c': 3, 'd': 4},
    {'a': 1, 'b': 2, 'c': 3, 'd': 4},
    {'a': 1, 'b': 2, 'c': 3, 'd': 4},
]
with open('c.csv', 'w', newline="") as f:
    f_csv = csv.DictWriter(f, headers)
    f_csv.writeheader()
    f_csv.writerows(rows)

print('csv 产生的数据都是字符串类型的，不会做其他类型的转换')
print('需要手动去实现')
col_types = [str, int, float, int]
with open('c.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        row = tuple(convert(value) for convert, value in zip(col_types, row))
        print(row)
print('只转换部分字段')
field_types = [('a', str),
               ('b', float),
               ('c', int)]
with open('c.csv') as f:
    for row in csv.DictReader(f):
        row.update((key, conversion(row[key]))
                   for key, conversion in field_types)
        print(row)

print('\n')
print('=' * 20)
print('pandas 中 有更好的 csv 处理方法')
