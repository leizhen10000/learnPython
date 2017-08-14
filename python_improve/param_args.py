#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Zhen Lei on 2017/8/12


# *args 和 **kwargs 主要用于函数定义，可以将不定数量的参数传递给一个函数
# 前提就是，在写函数的时候，不确定会有多少参数传递进来，所以使用这两个关键字。
# *args 是用来发送一个非键值对的可变参数列表给函数，**kwargs表示键值对


def var_args(f_arg, *args):
    print ("first normal arg: ", f_arg)
    for arg in args:
        print ("another arg through *args", arg)


# **kwargs 允许你将不定长度的键值对，作为参数传给一个函数。
def greet_me(*args, **kwargs):
    for arg in args:
        print ("list of key: ", arg)
    for key, value in kwargs.items():
        print ("{0} == {1}".format(key, value))


# 结合 *args 和 **kwargs
def some_func(fargs, *args, **kwargs):
    # pdb.set_trace()
    print ("first normal arg: ", fargs)
    for arg in args:
        # pdb.set_trace()
        print ("another arg through *args", arg)
    for key, value in kwargs.items():
        # pdb.set_trace()
        print ("{0} == {1}".format(key, value))


# 那么在什么时候能使用上这些方法呢
# 最常见的就是再写函数装饰器的时候，此外它还可以用来做猴子补丁（monkey patching）
# 猴子补丁的意思就是在程序运行是（runtime）的修改某些代码


# debugging Python 有一个debug的系统，不是在 pycharm 中集成的，是可以直接在代码中执行的
# Python debugger（pdb）
# 运行命令 python -m pdb my_script.py

if __name__ == '__main__':
    # var_args('yasoob', 'python', 'eggs', 'test')
    # greet_me('python', 'eggs', name='yasoob')
    some_func('yasoob', 'python', name='test')
