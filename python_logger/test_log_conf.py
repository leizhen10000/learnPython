#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2017/11/3 13:33
# @Author  : Lei Zhen 
# @Contract: leizhen8080@gmail.com
# @File    : test_log_conf.py
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
from config import logger

if __name__ == '__main__':
    logger.debug('debug message')
    logger.info('info message')
    logger.error('error message')
