#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2017/11/2 13:21
# @Author  : Lei Zhen 
# @Contract: leizhen8080@gmail.com
# @File    : read_file.py
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
import re


def add_dot():
    result_str = ''
    for line in open("/Users/leizhen/Downloads/test.txt"):
        result_str = result_str + insert_dot_in_line(line)
    print result_str


def insert_dot_in_line(str):
    return re.sub(r'\s', ',', str)


if __name__ == '__main__':
    add_dot()
    # print pat_dot('123 34')
