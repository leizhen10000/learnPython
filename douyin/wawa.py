#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
# @Time    : 19/11/20 19:44
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @Site    : http://www.leizhen.com
# @File    : wawa.py
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
import time

import pyautogui

from douyin.drag_mouse import check_user_in_db, hua, head_to_tail, back, focus_console

if __name__ == '__main__':
    # hua(10, head_to_tail, step=2)
    #
    # focus_console()
    # pyautogui.moveTo(1004, 633)
    # x = input('轻移动鼠标到某个标题栏：')
    # if x:
    #     pyautogui.click(pyautogui.position())
    #
    # time.sleep(.5)

    print(check_user_in_db())
