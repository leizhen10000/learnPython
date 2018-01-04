#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2017/11/3 13:29
# @Author  : Lei Zhen 
# @Contract: leizhen8080@gmail.com
# @File    : config.py.py
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
import logging.config

import yaml

# with open('logging.yml','r') as f_conf:
#     dict_conf = yaml.load(f_conf)
# logging.config.dictConfig(dict_conf)
# logger = logging.getLogger('simpleExample')

# 读取日志配置文件内容
logging.config.fileConfig('logging.conf')

# 创建一个日志器logger
logger = logging.getLogger('simpleExample')

if __name__ == '__main__':
    logger.debug('debug message')
    logger.info('info message')
    logger.warn('warn message')

    # 日志输出
    logger.debug('debug message')
    logger.info('info message')
    logger.warn('warn message')
    logger.error('error message')
    logger.critical('critical message')
