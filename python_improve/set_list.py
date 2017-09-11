#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Zhen Lei on 2017/9/10


# set 是一个非常有用的数据接口。它与 list 的行为类似，区别在于 set 不能包含重复的值。

def show_repeat_key():
    some_list = ['a', 'b', 'c', 'd', 'e', 'f', 'b', 'c', 'a']
    duplicates = set([x for x in some_list if some_list.count(x) > 1])
    print duplicates


# 交集
def same_between_collection():
    valid = set(['yellow', 'red', 'blue', 'green', 'black'])
    input_set = set(['red', 'brown'])
    print input_set.intersection(valid)  # 比较两个集合的交集


# 差集
def difference_between_collection():
    valid = set(['yellow', 'red', 'blue', 'green', 'black'])
    input_set = set(['red', 'brown'])
    print input_set.difference(valid)  # 只会输出input_set 中不同的值


class SetAndList():
    def __init__(self):
        pass


if __name__ == '__main__':
    show_repeat_key()
    same_between_collection()
    difference_between_collection()
