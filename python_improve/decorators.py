#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Zhen Lei on 2017/9/11

# 装饰器 Decorator 是 Python 的一个重要部分，简单的说，他是修改其他函数的功能的函数。
# Decorator 是最难掌握的概念之一，接下来会详细的讨论

# 一切皆对象
def hi(name="yasoob"):
    return "hi " + name


# 从函数中返回函数
def hi2(name="yasoob"):
    print "now you are inside the hi() function"

    def greet():
        return "now you are in the greet() function"

    def welcome():
        return "now you are in the welcome() funtion"

    if name == "yasoob":
        return greet
    else:
        return welcome


# 将函数作为参数传给另一个函数
def doSomethingBeforeHi(func):
    print "I am doing some boring work before executing hi()"
    print func()


class DecoratorInPython():
    def __init__(self):
        pass


if __name__ == '__main__':
    print hi()
    greet = hi
    print greet()
    a = hi2()
    print a
    print a()
    doSomethingBeforeHi(hi)
