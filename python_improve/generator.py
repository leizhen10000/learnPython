#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Zhen Lei on 2017/8/12


# 生成器（Generators）
# 首先要了解迭代器（iterators），可以遍历一个容器（尤其是列表）的对象

# 可迭代对象（Iterable）
# Python 中任意的对象，它只要定义了可以返回一个迭代器的__iter__方法，或者定义了可以支持下标索引的__getitem__方法，
# 那么他就是一个可迭代对象，简单的说，可迭代对象就是能提供迭代器的任意对象

# 迭代器（Iterator）
# 任意对象，只要定义了 next 或者 __next__ 方法，它就是一个迭代器

# 迭代（Iteration）
# 当我们使用一个循环来遍历某个东西时，这个过程本身就叫迭代

# 生成器 也是一种迭代，但是只能迭代一次，因为他是在运行时 yield 值
def generator_function():
    for i in range(10):
        yield i


# 生成器最佳应用场景：你不想同一时间将所有计算出来的大量结果分配到内存中，特别是结果集还包含循环
# 下面是一个计算斐波那契数列的生成器
def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    # for item in generator_function():
    #     print item
    # for x in fibon(2):
    #     print x
    my_string = "yasoob"
    # 此时 str 对象不是一个迭代器，或者说他是一个可迭代对象，而不是一个迭代器。
    # 这就意味着他支持迭代，但我们不能直接对其进行迭代操作。
    # 可以通过一个内置函数 iter，根据一个可迭代对象返回一个迭代器对象。
    my_iter = iter(my_string)
    print next(my_iter)
