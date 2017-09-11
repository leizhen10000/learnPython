#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Zhen Lei on 2017/9/11


# 三目运算符通常在 Python 里被称为条件表达式，这些表达会基于 true/not 的条件判断，在 Python 2.4 中才有三元操作

def trinity_operation():
    is_fat = True
    state = "fat" if is_fat else "not fat"
    print state


if __name__ == '__main__':
    trinity_operation()
