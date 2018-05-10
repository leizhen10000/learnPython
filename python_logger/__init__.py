#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2017/11/3 10:40
# @Author  : Lei Zhen 
# @Contract: leizhen8080@gmail.com
# @File    : __init__.py.py
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
# 日志文件系统，是阅读 loging 模块源码，重新敲一次代码，便于了解

__status__ = "copy"
__version__ = "1.0.0"
__date__ = "2018/04/09"

# -------------------------------------------------------------------
#     日志等级划分
# -------------------------------------------------------------------

CRITICAL = 50
FATAL = CRITICAL
ERROR = 40
WARNING = 30
WARN = WARNING
INFO = 20
DEBUG = 10
NOTSET = 0

_levelToName = {
    CRITICAL: 'CRITICAL',
    ERROR: 'ERROR',
    WARNING: 'WARNING',
    INFO: 'INFO',
    DEBUG: 'DEBUG',
    NOTSET: 'NOTSET'
}
_nameToLevel = {
    'CRITICAL': CRITICAL,
    'FATAL': FATAL,
    'ERROR': ERROR,
    'WARN': WARNING,
    'WARNING': WARNING,
    'INFO': INFO,
    'DEBUG': DEBUG,
    'NOTSET': NOTSET
}


def get_level_name(level):
    """
    返回 表示日志级别的文本

    如果 level 为预设的等级(CRITICAL,ERROR,WARNING,INFO,DEBUG)，就会返回对应的 string
    文本，如果是通过 addLevelName 方法新增了级别，则会返回对应级别的名称。

    如果是一个数字级别的等级，则返回关联的等级名称。

    否则，就会返回 "Level %s" % level 的内容
    """
    result = _levelToName.get(level)
    if result is not None:
        return result
    result = _nameToLevel.get(level)
    if result is not None:
        return result
    return "Level %s" % level

def add_level_name(level,level_name):
    """
    关联 等级 和 名称

    转变名称为数值等级
    :param level:
    :param level_name:
    :return:
    """


if __name__ == '__main__':
    print(get_level_name('CRITICAL'))
    print(get_level_name('SOME'))
