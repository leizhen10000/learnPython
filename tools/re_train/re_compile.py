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
import re


# compile 是一个工厂类方法，用于将字符串形式的正则表达式编译成 Pattern 对象。
# 第二个参数 flag 可选，匹配模式

class ReCompile:
    def __init__(self):
        self._str = 'Hi, nice to meet you where you from ?'

    def compile_1(self):
        pattern = re.compile(r'\w*o\w*')  # 匹配带o的字符串
        print pattern.findall(self._str)  # 显示所有包含 o 的字符串
        print pattern.sub(lambda m: '[' + m.group(0) + ']', self._str)  # 把字符串中含有 o 的单词用 [] 括起来

    def compile_2(self):
        match = re.match(r'\w*', self._str)
        print match.group(0)

    # X verbose 详细模式，这个模式下正则表达式可以多行，忽略空白字符，并且可以加入注释
    def compile_3(self):
        str = '1.5623165'
        pattern = re.compile(r'''\d +  # the integral part
                                 \.    # the decimal point
                                 \d *  # som fractional digits''', re.X)
        pattern_1 = re.compile(r'\d+\.\d*')  # 跟上面是同一个功能
        match = pattern_1.match(str)
        if match:
            print match.group()
        else:
            print match


if __name__ == '__main__':
    ReCompile().compile_1()
    ReCompile().compile_2()
    ReCompile().compile_3()
