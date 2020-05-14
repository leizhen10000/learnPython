#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'leizhen'
__mtime__ = '2017/8/11'
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


def split_url_2_class_name(url):
    # test = '/rider/obtain-good.json'
    result = re.split(r'[./]', url)[-2]
    method_list = re.split(r'-', result)
    name = ''
    for item in method_list:
        name += item.title()
    return name


class ReSplit:
    def __init__(self):
        pass

    def split_1(self):
        result = re.split('\w+', 'test, test, test.')
        for item in result:  # 匹配任意非数字和字母，相当于 [a-z A-Z 0-9],所以返回结果为逗号
            print(item)

    def split_2(self):
        test = 'Hi, nice to meet you where are you from ?'
        result = re.split(r'\s+', test)  # 匹配任意空白字符，相当于 [\t\n\r\f\v]
        print(result)


if __name__ == '__main__':
    ReSplit().split_1()
    ReSplit().split_2()
    print(split_url_2_class_name('/rider/obtain-good.json'))
