#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@file    :  pipe_machine_iterator.py
@time    :  20/2/16 18:03
@author  :  leizhen
@contact :  leizhen8080@foxmail.com
@desc    :  以数据管道的方式迭代处理数据
"""

# 如果有海量的数据需要处理
import fnmatch
import itertools
import os
import re


def get_find(file_pat, top):
    """获取所有的文件，正则匹配文件名称"""
    for path, dir_list, file_list in os.walk(top):
        for name in fnmatch.filter(file_list, file_pat):
            yield os.path.abspath(os.path.join(path, name))


def gen_opener(file_names):
    """文件名序列，并生成文件对象
    在下一次迭代前立即关闭文件"""
    for file_name in file_names:
        f = open(file_name, 'rt', encoding='utf-8')
        yield f
        f.close()


def gen_concatenate(iterators):
    """将所有的单个文件序列连成一个单独的序列"""
    for it in iterators:
        yield from it


def gen_grep(pattern, lines):
    """匹配文件序列的全部行中内容"""
    pat = re.compile(pattern)
    for n, line in enumerate(lines, 1):
        if pat.search(line):
            yield n, line


log_names = get_find('*.log*', '../../mylog')
files = gen_opener(log_names)
lines = gen_concatenate(files)
real_lines = gen_grep('(?i)面膜', lines)

for n, real_line in itertools.islice(real_lines, None, 50):
    print(n, real_line)
