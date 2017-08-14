#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'leizhen'
__mtime__ = '2017/8/10'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""

# Python 通过 re 模块提供对正则表达式的支持。使用 re 的一般步骤是先将正则表达式的字符形式编译成 Pattern 实例，然后使用
#  Pattern 实例处理文本并获得匹配结果（一个 Match 实例），最后使用 Match 实例获的信息，进行其他的操作。
import re


def re_in_python():
    # 1. 将正则表达式编译成 Pattern 对象
    pattern = re.compile(r'hello')
    # compile 是一个工厂类方法，用于将字符串形式的正则表达式编译成 Pattern 对象。
    # 第二个参数 flag 可选，匹配模式

    # 2. 使用 Pattern 匹配文本，获得匹配结果，无法匹配时将返回 None
    match = pattern.match('hello world!')
    # Match 对象是第一次匹配结果，包含了很多关于此次匹配的信息

    # 3. 使用 Match 获取分组信息
    if match:
        print match.group()


if __name__ == '__main__':
    re_in_python()
