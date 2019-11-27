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
logger_wei = logging.getLogger('wei')


class Logger():

    def __init__(self, log):
        self.logger = log

    def debug(self, *args):
        return self.logger.debug(*args)

    def info(self, *args):
        return self.logger.info(*args)

    def warn(self, *args):
        return self.logger.warning(*args)

    def error(self, *args, **kwargs):
        return self.error(*args, **kwargs)
