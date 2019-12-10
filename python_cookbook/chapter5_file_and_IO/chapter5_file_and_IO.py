#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
# @Time    : 19/11/7 14:14
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @Site    : http://www.leizhen.com
# @File    : chapter5_file_and_IO.py
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
# 使用迭代的方式读取文件
import glob
import io
import mmap
import os
from array import array
from functools import partial
from tempfile import TemporaryFile, TemporaryDirectory

f = open('book.txt')
for line in iter(lambda: f.read(50), ''):
    print(line)
f.close()

print('=' * 20)
print('只读模式')
print('将整个文件作为一行读取')
with open('book.txt', 'rt') as f:
    data = f.read()
    print(data)
print('迭代每一行')
with open('book.txt', 'rt') as f:
    for line in f:
        print(line)
print('=' * 20)
print('输出内容到文件')
with open('输出到文件.txt', 'wt', encoding='utf-8') as f:
    print('新建一行文本', file=f)
print('\n')
print('=' * 20)
print('活用 print')
print('end 和 sep 关键字')
print('NAME', 20, 1.5, sep=',', end=' <<<\n')
print('禁止换行')
for i in range(1, 4):
    print(i, ' ')
print('替代 join 拼接的不便，如可以非字符串类型共同输出')
keys = [12, 'name', list('abc')]
print(*keys, sep=',')

print('\n')
print('=' * 20)
print('读取字节数据')
print('读取文本为一行，使用 rb 模式')
with open('a.info', 'rb') as f:
    print(f.read().decode('utf-8'))

with open('b.info', 'wb') as f:
    f.write('我与地坛\n史铁生\n励志\n人生思考\n'.encode('utf-8'))

print('\n')
print('=' * 20)
print('数组和C结构体类型能被直接写入，而不用中间转换为自己对象')
print('写入')
nums = array('i', [1, 2, 3, 4])
print(nums)
with open('data.bin', 'wb') as f:
    f.write(nums)
print('读取')
with open('data.bin', 'rb') as f:
    print(f.read().decode('utf8'))
print('无法读取真实内容')
print('真实的读取方法')
a = array('i', [0, 0, 0, 0, 0, 0, 0])
with open('data.bin', 'rb') as f:
    f.readinto(a)
print(a)
print('读取二进制数据到底层的内存中去')

print('\n')
print('=' * 20)
print('x 模式，在文件不存在的时候才能写入，不允许覆盖已经存在的文件')

print('\n')
print('=' * 20)
print('字符串的 I/O 操作')
s = io.StringIO()
print(s.write('全自动洗衣机\n'))
print('低耗能', file=s)
print(s.getvalue())
print('读取内容')
s = io.StringIO('权力的游戏')
print(s.read(8))

print('\n')
print('=' * 20)
print('读取固定大小')
with open('b.info', 'rb') as f:
    records = iter(partial(f.read, 320), b'')
    for r in records:
        print(r.decode('utf-8'))

print('\n')
print('=' * 20)
print('读取二进制到可变缓冲区中')


def read_into_buffer(filename):
    buf = bytearray(os.path.getsize(filename))
    with open(filename, 'rb') as f:
        f.readinto(buf)
    return buf


buf = read_into_buffer('data.bin')
print(buf)

print('\n')
print('=' * 20)
print('映射二进制文件到一个可变字节数组中')


def memory_map(filename, access=mmap.ACCESS_WRITE):
    size = os.path.getsize(filename)
    fd = os.open(filename, os.O_RDWR)
    return mmap.mmap(fd, size, access=access)


size = 100000
with open('data', 'wb') as f:
    f.seek(size - 1)
    f.write(b'\x00')

m = memory_map('data')
print(len(m))
print(m[:10])
m[:11] = b'Hello World'
m.close()
with open('data', 'rb') as f:
    print(f.read(11))

print('\n')
print('=' * 20)
print('路径的最后一个元素')
print(os.path.basename('a.info'))
print('获取路径名称')
print(os.path.dirname(os.path.abspath('a.info')))
print('拆分文件拓展名')
print(os.path.splitext(os.path.abspath('a.info')))
print(os.path.split(os.path.abspath('a.info')))
print(os.path.splitdrive(os.path.abspath('a.info')))
print('获取文件夹中的文件列表')
print(os.listdir(os.path.split(os.path.abspath('a.info'))[0]))
pyfiles = glob.glob('*.py')
print(pyfiles)

print('\n')
print('=' * 20)
print('创建匿名文件')
with TemporaryFile('w+t') as f:
    f.write('hello')
    f.write('world')
    f.write('test\n')
    f.seek(0)
    data = f.read()
    print(data)
print('创建临时匿名目录')
with TemporaryDirectory() as dirname:
    print('dirname is : ', dirname)
