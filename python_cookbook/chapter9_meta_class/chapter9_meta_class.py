#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2019/11/11 06:58
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @File    : chapter9_meta_class.py
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
import contextlib

print('内置库 contextlib 库')
print('装饰器 contextmanager。在 yield 语句前的代码作为 __enter__ 方法执行，之后的代码作为 __exit__ 方法执行')


@contextlib.contextmanager
def open_func(file_name):
    # __enter__ 方法
    print('open file: ', file_name, 'in __enter__')
    file_handler = open(file_name, 'r')

    yield file_handler

    # __exit__ 方法
    print('close file: ', file_name, 'in __exit__')
    file_handler.close()
    return


with open_func('test.txt') as file_in:
    content = file_in.read()
    print(content)
    # raise ZeroDivisionError

print('closing 类，自动调用传入对象的 close 方法')


class MyOpen2:

    def __init__(self, file_name):
        self.file_handler = open(file_name, 'r')
        return

    def close(self):
        print('call close in MyOpen2')
        if self.file_handler:
            self.file_handler.close()
        return


with contextlib.closing(MyOpen2('test.txt')) as file_in:
    print(file_in)

# nested 类
print('nested 类')
with open('test.txt') as file_in, open('test1.txt') as file_out:
    print(file_in.read())
    print(file_out.read())
