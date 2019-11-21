#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
# @Time    : 19/11/21 10:50
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @Site    : http://www.leizhen.com
# @File    : conver_encoding.py
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
import os


def convert_file():
    file_list = os.listdir('D:\douyin')
    for file in file_list:
        file_name = os.path.join('D:\douyin', file)
        with open(file_name, 'rb') as f:
            res = f.read().decode('utf-16-le').encode('utf-8').decode('utf-8-sig')
        with open(os.path.join('D:\douyin2', file), 'w', encoding='utf-8') as fw:
            fw.write(res)


convert_file()
