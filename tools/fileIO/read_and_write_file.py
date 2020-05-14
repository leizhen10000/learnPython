#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'leizhen'
__mtime__ = '2017/6/27'
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


class ReadAndWriteFile(object):
    def __init__(self):
        self._file_abs = "E:\\test.txt"

        pass

    def read_file(self):
        f = open(self._file_abs, "r")
        try:
            print(f.read().decode("gbk"))
        finally:
            if f:
                f.close()

    def simple_read_file(self):
        with open(self._file_abs, "r") as f:
            poetry_list = f.readlines()
        for i in poetry_list:
            print(i.decode("gbk"))

    def write_file(self):
        with open(self._file_abs, "a") as f:
            f.write("Hello World!")


if __name__ == '__main__':
    # ReadAndWriteFile().read_file()
    # ReadAndWriteFile().write_file()
    ReadAndWriteFile().simple_read_file()
