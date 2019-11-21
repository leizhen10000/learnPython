#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
# @Time    : 19/11/20 17:34
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @Site    : http://www.leizhen.com
# @File    : drag_mouse.py
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
# 屏幕分辨率
import math
import time
from random import random, randrange, sample, choice

import pyautogui as m

width, height = m.size()


# m.moveTo(300, 300, duration=.25)

def draw_cycle():
    r = 250
    # 圆心
    o_x = width / 2
    o_y = height / 2

    pi = math.pi

    for i in range(2):  # 转两圈
        for angle in range(0, 360, 5):
            x = o_x + r * math.sin(angle * pi / 180)
            y = o_y + r * math.cos(angle * pi / 180)

            m.moveTo(x, y, duration=.1)


x, y = 813, 157
back_pos = x, y
head = x + 762, y + 55
tail = x + 762, y + 1630
aweme_one = x + 300, y + 400
aweme_two = x + 300, y + 955
aweme_three = x + 300, y + 1400
right = x + 800 + randrange(0, 50, 3), y + 300 + randrange(0, 1200, 3)
left = x + 100 + randrange(0, 50, 3), right[1] + randrange(0, 10, 2)

console = 2589, 2055
copy_translate = 2358, 2048  # 截图识别文字后，点击复制
aweme_list_button = x + 450, y + 630

time_sample = [0.01, 0.021, 0.031, 0.023]
time_1 = 0.1 + choice(time_sample)
time_2 = 0.2 + choice(time_sample)
time_3 = 0.3 + choice(time_sample)
time_4 = 0.4 + choice(time_sample)
time_5 = 0.5 + choice(time_sample)
time_8 = 0.8 + choice(time_sample)
time_10 = 1.0 + choice(time_sample)
time_20 = 2.0 + choice(time_sample)


def back():
    m.click(x, y)


def fly_left():
    # 向左滑动
    m.moveTo(right[0], right[1], duration=time_1)
    m.dragTo(left[0] - 300, left[1], duration=time_3)


def fly_right():
    # 向右滑动
    m.moveTo(left[0], left[1], duration=time_1)
    m.dragTo(right[0] + 300, right[1], duration=time_1)


def head_to_tail():
    """向下滑动，从上到下"""
    m.moveTo(head[0], head[1])
    m.dragTo(tail[0], tail[1], duration=time_2)


def tail_to_head():
    """向上滑动，从下到上"""
    m.moveTo(tail[0], tail[1])
    m.dragTo(head[0], head[1], duration=time_8)


def hua(exec_count, hua_method):
    """控制 hua 划的次数"""
    print(time.strftime('%H:%M:%S'))
    count = math.ceil(exec_count / 9) + 1

    while count > 0:
        print('计数', count)
        count -= 1
        hua_method()


# 控制台相关功能
def change_window():
    m.hotkey('alt', 'tab')


def run_script():
    m.hotkey('ctrl', 'F5')


def stop_script():
    m.hotkey('ctrl', 'F2')


def translate_word():
    m.hotkey('ctrl', 'alt', 'p')
    m.doubleClick(head[0], head[1])


def focus_console():
    m.moveTo(console[0], console[1], duration=.5)
    m.click(console[0], console[1])


def get_suren_info():
    """获取素人信息，判断是否有橱窗

    有则获取橱窗信息和作品信息
    """
    time.sleep(time_20)
    fly_left()  # 向左滑动，进入主页 tip：可能不需要这步骤
    # 判断是否有商品橱窗
    focus_console()
    has_aweme = int(input('请判断是否有橱窗'))
    if has_aweme:
        # 点击橱窗
        m.moveTo(aweme_list_button[0], aweme_list_button[1])
        click_or_not = int(input('是否自由点击橱窗'))
        if click_or_not:
            input('点击完成？')
            focus_console()
        else:
            m.click(aweme_list_button[0], aweme_list_button[1])
        time.sleep(time_10)
        focus_console()
        promotion_amount = int(input('商品总数:'))
        if promotion_amount > 10:
            hua(promotion_amount, tail_to_head)
        # 返回作品界面
        back()
        time.sleep(time_4)
        # 作品向上滑动
        m.moveTo(console[0], console[1])
        m.click(console[0], console[1])
        aweme_num = int(input('请输入作品总数'))
        hua(aweme_num, tail_to_head)
        # 返回视频界面
        back()
        time.sleep(time_1)
        # 返回消息列表
        back()
        time.sleep(time_2)
    else:
        back()
        time.sleep(time_3)
        back()
        time.sleep(time_3)


def roll_page():
    m.moveTo(head[0], head[1], duration=time_1)
    m.dragTo(tail[0], tail[1], duration=time_1)


def action():
    """流程"""
    # 点击第一个视频
    m.click(aweme_one[0], aweme_one[1], duration=time_1)
    get_suren_info()
    # 点击第二个视频
    m.click(aweme_two[0], aweme_two[1], duration=0.2 + random() / 3.0)
    get_suren_info()
    m.click(aweme_three[0], aweme_three[1], duration=.2 + random() / 2.0)
    get_suren_info()
    # time.sleep(time_10)


if __name__ == '__main__':
    roll_times = 0
    while True:
        focus_console()
        is_continue = int(input('是否继续'))
        if is_continue:
            # m.hotkey('alt', 'tab')
            roll_page()
            roll_times += 1
            print(f'翻页次数 {roll_times}')
            action()

    # m.hotkey('alt', 'tab')
    # # draw_cycle()
    # if is_continue:
    #     m.hotkey('ctrl', 'F5')
    # print('ctrl+f2 停止')
