#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@file    :  escape_first_lines.py
@time    :  20/2/16 13:31
@author  :  leizhen
@contact :  leizhen8080@foxmail.com
"""

# 如果要便利一个对象，但是一开始的元素并不感兴趣

# with open('test.txt') as f:
#     for line in f:
#         print(line)

from itertools import dropwhile

with open('test.txt') as f:
    for line in dropwhile(lambda l: 'python' in l, f):
        print(line, end='')

print('python'.__contains__('p'))

