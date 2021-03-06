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
import json

import os
import random
import time
from math import ceil

import pyautogui

from douyin.drag_mouse import check_user_in_db, hua, head_to_tail, back, focus_console, tail_to_head_aweme, \
    check_convert_file_exits, pre_check_sql, douyin_run


class Following:

    def __init__(self):
        self.following_num = 0
        self.useful_user_num = 0
        following_users = self.get_following_users()
        # 先获取默认的关注用户20个，取得关注总数
        list(self.parse_following_users(following_users))
        self.down_and_up()
        # 重新获取需要的更多关注用户
        self.hit_user_indexes = list(self.parse_following_users(self.get_following_users()))
        print(self.hit_user_indexes)
        print(self.following_num)
        self.usage_ratio = self.useful_user_num / float(self.following_num)
        print(self.usage_ratio)
        if self.usage_ratio > .002:
            self.click_user_in_following_esc()

    def get_following_users(self):
        """获取 关注列表"""
        check_convert_file_exits(file_tags='following')
        file_list = os.listdir('d:\\douyin2')
        following_files = list(filter(lambda x: 'following' in x, file_list))
        # following_files = list(map(lambda x: os.path.join('d:\\douyin2', x), following_files))
        for file_name in following_files:
            file_dir = os.path.join('d:\\douyin2', file_name)
            with open(file_dir, encoding='utf-8') as f:
                for line in f:
                    if not line.strip().strip('\n'):
                        continue
                    data = json.loads(line)
                    following_users = data.get('followings')
                    total = data.get('total')
                    if int(total) == 0:
                        continue
                    self.following_num = int(total)
                    if following_users:
                        yield from following_users

    def down_and_up(self):
        # 先上下滑动获取关注用户，200为界
        if self.following_num < 200:
            true_num = self.following_num
        else:
            print('关注量大于200，取前300')
            true_num = 300  # 真实获取用户量
        x, y = 791, 155
        head = x + 762, y + 81
        tail = x + 762, y + 1630

        down_times = ceil(true_num / 80)
        up_times = ceil(true_num / 20)

        # 上划
        for i in range(up_times):
            new_x = head[0] + random.randint(-400, 100)
            pyautogui.moveTo(new_x, tail[1] + random.randint(-300, 20))
            pyautogui.dragTo(new_x + random.randint(30, 50), head[1] + random.randint(-100, -80),
                             duration=random.randint(2, 4) / 56.0)
            time.sleep(.3)

        # 下滑
        for i in range(down_times):
            new_x = head[0] + random.randint(50, 100)
            pyautogui.moveTo(new_x, head[1] + 1200)
            pyautogui.dragTo(new_x, tail[1], duration=.1)
            time.sleep(1)

    def parse_following_users(self, following_users):
        """解析用户"""
        line = 0
        num = 0
        for user in following_users:
            uid = user.get('uid')
            nickname = user.get('nickname')
            has_promotion = user.get('with_fusion_shop_entry')
            unique_id = user.get('unique_id', '')  # 抖音号
            short_id = user.get('short_id', '')  # 抖音号2
            if not unique_id:
                unique_id = short_id
            enterprise_verify_reason = user.get('enterprise_verify_reason')  # 官方认证，蓝V
            if enterprise_verify_reason != '':
                # num += 1
                line += 1
                continue
            enterprise_verify_reason = user.get('enterprise_verify_reason')  # 官方认证，蓝V
            if has_promotion and nickname != '已重置':
                user_info = {'name': nickname, 'aweme_count': 20, 'suren_id': uid}
                user_info = pre_check_sql(user_info)
                if user_info.get('flag') is False:
                    num += 1
                    print('N', num, 'l', line, '用户', '【', nickname, '】', unique_id, '拥有橱窗')
                    if line % 10 == 0:
                        print('第十个分割线', '=' * 30)
                    yield line
            line += 1
            self.useful_user_num = num

    def click_user_in_following(self):
        """点击关注中指定的用户
        指定的用户列表
        """
        max_user = self.following_num
        hit_users = self.hit_user_indexes

        x_space = 1247 + random.randint(-100, 200)
        y = 1945
        y_height = 172  # 每个用户移动的高度

        # 首先移出最底端提示
        pyautogui.moveTo(x_space, y - 170)
        pyautogui.drag(xOffset=random.randint(-10, 10), yOffset=150, duration=1)

        max_page = max_user // 10  # 最后一页是主页
        if max_user <= 12:  # 如果少于12个用户，直接可以在当前页点击，默认为一页
            max_page = 1

        cur_page = 0
        # 移动到指定用户
        # todo: 最多一次跨越10
        y_step = 9

        hit_users = sorted(hit_users, reverse=True)
        for user_num in hit_users:
            if max_page == 1:  # 如果在13以内，之间可以点击，而不必滑动
                pyautogui.click(x=x_space, y=y - 50 - (12 - user_num) * 150, duration=.5)
                douyin_run()
                continue
            move_steps = max_user - user_num - cur_page * 10
            # if move_steps < 10:
            #     pyautogui.moveTo(x_space, y=y + 80 - move_steps * y_height, duration=.5)
            #     time.sleep(3)
            # else:  # 否则翻页
            page_steps = move_steps // 10
            for i in range(page_steps):
                pyautogui.moveTo(x_space, y - y_step * y_height)
                pyautogui.drag(xOffset=random.randint(-10, 10), yOffset=y_step * y_height, duration=3)
            cur_page += page_steps
            # 进入对应页面后点击
            pyautogui.moveTo(x_space, y - 50 - (move_steps % 10) * 150, duration=.5)
            douyin_run()
            time.sleep(1)
            # 如果在最后一页了，最后一页内容舍弃
            if cur_page == max_page - 1:
                break

    def click_user_in_following_esc(self):
        """上面一个倒着来的方法太蠢了，还是正着获取内容"""
        max_user = self.following_num

        x_space_up = 1247 + random.randint(-100, 200)
        y_up = 287
        y_height = 187.79  # 每个用户拖拽移动的高度，不同电脑里面可能不同
        y_real_height = 150  # 每个用户的真实高度
        y_step = 9
        cur_page = 0  # 定位当前页
        hit_users = sorted(self.hit_user_indexes)

        max_page = max_user // 10

        for user_num in hit_users:
            # 相对于当前的页面，需要多翻页多少，选取多少
            page_steps, move_steps = divmod(user_num - cur_page * 10, 10)
            for i in range(page_steps):
                pyautogui.moveTo(x_space_up, y_up + (y_step - 1) * y_height)
                if i == 0:
                    pyautogui.drag(xOffset=0, yOffset=-y_step * y_height - 10,
                                   duration=1.01, tween=pyautogui.easeOutQuad)
                else:
                    pyautogui.drag(xOffset=0, yOffset=-y_step * y_height, duration=1.01, tween=pyautogui.easeOutQuad)
                pyautogui.moveTo(x_space_up, y_up + y_height)
                # pyautogui.scroll(clicks=11, x=x_space_up, y=y_up + y_height)
                time.sleep(.1)
            cur_page += page_steps
            if cur_page + 1 == max_page:
                break
            pyautogui.moveTo(x=x_space_up, y=y_up + y_real_height * move_steps)
            suren_info = douyin_run()
            # missing_position = 0
            # if suren_info.get('has_next_action') is False:
            #     missing_position += 1
            # else:
            #     missing_position = 0
            # if missing_position > 2:
            #     raise Exception('用户偏移出错，请检查')
            time.sleep(.3)


def click_fans():
    """点击粉丝"""

    pass

if __name__ == '__main__':
    follow = Following()
    # user_gen = follow.get_following_users()
    # user_nums = list(follow.parse_following_users(user_gen))
    # print(user_nums)
    # follow.click_user_in_following()
    # hua(50, head_to_tail, step=9)
    # head_to_tail(duration=0.2)
    # focus_console()
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
