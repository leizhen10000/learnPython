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
import ctypes
import time

import pyautogui

from douyin.drag_mouse import check_user_in_db, hua, head_to_tail, back, focus_console

if __name__ == '__main__':
    hua(10, head_to_tail, step=2)

    focus_console()
    # for i in range(2):
    #     x, y = 1061, 1607
    #     convertX, convertY = 65536 * x // 3840 + 1, 65536 * y // 2160 + 1
    #     ctypes.windll.user32.SetCursorPos(x, y)
    #     ctypes.windll.user32.mouse_event(2, convertX, convertY, 0, 0)
    #     time.sleep(0.8)
    #     ctypes.windll.user32.mouse_event(4, convertX, convertY, 0, 0)
    #
    #     delete_x, delete_y = 1274, 1284
    #     pyautogui.moveTo(delete_x, delete_y, duration=.5)
    #     pyautogui.click(delete_x, delete_y)
    #
    #     time.sleep(.8)

    # x = input('轻移动鼠标到某个标题栏：')
    # if x:
    #     pyautogui.click(pyautogui.position())
    #
    # time.sleep(.5)
    #
    # print(check_user_in_db())
