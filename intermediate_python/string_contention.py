#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
# @Time    : 2019/1/5 09:41
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @Site    : http://www.leizhen.com
# @File    : string_contention.py
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
names = ['Jeff', 'Gary', 'Jill', 'Samantha']

for name in names:
    statement = 'Hello there' + name
    print(statement)

"""
This is easily read, but unfortunately not the ideal choice.
这种方法简单明了，但是不是最理想的选择。
Some people will conceed and let you do it if you're only adding two strings
together, and that's it. Instead, you should be using `.join`:
如果要拼接两个字符串，可以使用下面的方法
"""
for name in names:
    statement = ' '.join(['Hello there', name])
    print(statement)

"""
The reason for this is it scales better.
采取这种方式的原因，是它能更好的扩展。
When we use the +, we're creating new strings.
在使用 + 连接字符串的时候，我们创建了一个新的strings对象。
A more impactful example of this might be if we're just trying to print out 
a string list of all of the names:
"""

