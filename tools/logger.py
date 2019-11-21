#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
# @Time    : 19/11/19 17:19
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @Site    : http://www.leizhen.com
# @File    : logger.py
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
import json
import logging.config

import yaml

with open('../logging.yml', 'r') as f:
    config = yaml.load(f, Loader=yaml.SafeLoader)
    logging.config.dictConfig(config)

logger = logging.getLogger('tou')


def debug(*args):
    return logger.debug(*args)


def info(*args):
    return logger.info(*args)


def warn(*args):
    return logger.warning(*args)


def error(*args, **kwargs):
    return logger.error(*args, **kwargs)
