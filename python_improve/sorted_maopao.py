#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2019/11/8 06:51
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @File    : sorted_maopao.py
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
from random import randrange, shuffle

nums = [1, 3, 8, 2, 9, 5, 6, 4]
length = len(nums)
for i in range(length - 1):
    for j in range(length - 1 - i):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
print(nums)

array = []

while len(array) < 12:
    array.append(randrange(-99, 101, 3))
shuffle(array)

print(f'排序前数组:{array}')

for i in range(len(array) - 1):
    for j in range(len(array) - 1 - i):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]

print(f'排列后数组：{array}')

print('\n')
print('插入排序')
shuffle(array)
print(f'排序前数组：{array}')
for i in range(1, len(array)):
    key = array[i]
    j = i - 1
    while j >= 0 and key < array[j]:
        array[j + 1] = array[j]
        j -= 1
    array[j + 1] = key

print(f'排序后数组：{array}')

shuffle(array)
print(f'快速排序前数组：{array}')


def partition(a, l, r):
    x = a[r]
    i = l - 1
    for j in range(l, r):
        aa = a[j]
        if a[j] <= x:
            i += 1
            bb = a[i]
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[r] = a[r], a[i + 1]
    return i + 1


array = [8, 7, 2, 5, 6, 3]


def quick_sort(a, l, r):
    if l < r:
        q = partition(a, l, r)
        quick_sort(a, l, q - 1)
        quick_sort(a, q + 1, r)


quick_sort(array, 0, len(array) - 1)

print(f'快速排序后数组：{array}')

print('\n')
print('另一种快排方法')


def quick_sort1(a, l, r):
    if l >= r:
        return
    low, high = l, r
    key = a[low]
    while l < r:
        aa = a[r]
        while l < r and a[r] > key:
            r -= 1
        a[l] = a[r]
        while l < r and a[l] <= key:
            l += 1
        bb = a[l]
        a[r] = a[l]
    a[l] = key
    quick_sort1(array, low, l - 1)
    quick_sort1(array, l + 1, high)


array = [8, 2, 9, 5, 6, 3]
quick_sort1(array, 0, len(array) - 1)
print(f'快速排序后数组：{array}')
