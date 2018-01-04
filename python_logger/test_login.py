#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2017/11/3 10:48
# @Author  : Lei Zhen 
# @Contract: leizhen8080@gmail.com
# @File    : test_login.py
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
import unittest


class TestLogin(unittest.TestCase):
    def setUp(self):
        print ("++++++++++ test math class setup ++++++++++")

    def tearDown(self):
        print ("++++++++++ test math class teardown ++++++++++")

    def test_math_add(self):
        self.assertEqual('1', '1', 'test 1=1 fail')

    def test_math_add1(self):
        self.assertTrue('1', 'test true')

    def test_true(self):
        self.assertEqual(2, 2)


if __name__ == '__main__':
    unittest.main()
