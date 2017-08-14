#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Zhen Lei on 2017/8/14


# 大多数时候，我们把列表中所有元素一个个地传递给一个函数，并收集输出
# map 可以用一种简单而且漂亮的方式来实现，就是使用匿名函数（lambda）来配合map
def map_list():
    items = [1, 2, 3, 4, 5]
    squared = list(map(lambda x: x ** 2, items))
    return squared


# map 不仅可以用于一列表的输入，甚至可以用于列表函数的输入
def multiply(x):
    return x * x


def add(x):
    return x + x


def map_method():
    funcs = [multiply, add]
    for i in range(5):
        value = list(map(lambda m: m(i), funcs))
        print value
        # 上面 print 的时候，添加了list的转换，是为了 python2/3 的兼容性，在 python 2 中，map直接返回列表值，
        # 但是在 python 3 中返回迭代器，所以为了兼容，需要 list 转一下


# filter 就是过滤列表中的元素，并且返回所有符合条件的元素列表，符合条件即函数映射到该元素时返回值为True
def filter_method():
    number_list = range(-5, 5)
    less_than_zero = filter(lambda x: x < 0, number_list)
    print list(less_than_zero)
    # 如果 map 和 filter 对你来说看起来并不优雅的话，那么可以试一下后续会讲的 列表/字典/元组推导式


# reduce 一般用于类似于阶乘的场景
def reduce_method():
    product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
    print product
    # python 中你会使用基本的 for 循环来完成这个任务
    result = 1
    for i in range(1, 5):
        result *= i
    print result


# http://docs.pythontab.com/interpy/Map_Filter/Reduce/


if __name__ == '__main__':
    print map_list()
    filter_method()
    reduce_method()
