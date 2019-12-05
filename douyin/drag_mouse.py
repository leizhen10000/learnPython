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
import ctypes
import datetime
import json
import math
import os
import re
import threading
import time
import traceback
from functools import wraps
from random import random, randrange, sample, choice, randint

import pyautogui as m

from douyin.conver_encoding import convert_file, clean_dir
from douyin.extract_promotion_detail import handle_file
from tools.logger import logger
from tools.parser_config import get_db_tool

width, height = m.size()

# m.moveTo(300, 300, duration=.25)

log = logger


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


x, y = 791, 155
back_pos = x, y
head = x + 762, y + 81
tail = x + 762, y + 1630
aweme_one = x + 200 + randint(1, 5), y + 400
aweme_two = x + 130 + randint(5, 10), y + 850
# 分享用户标签时的位置，整个标签都可以点击
aweme_three = x + 135 + randint(-30, 190), y + 1400
# aweme_three = x + 322 + randint(-250, 130), y + 1527 + randint(-40, 50)
right = x + 800 + randrange(0, 50, 3), y + 300 + randrange(0, 1200, 3)
left = x + 100 + randrange(0, 50, 3), right[1] + randrange(0, 10, 2)
avatar = x + 976 + randint(-3, 3), y + 987 + randint(-3, 3)
delete_x, delete_y = x + 483 + randint(-80, 70), y + 1129 + randint(-5, 20)
# delete_x, delete_y = x + 483 + randint(-80, 70), y + 1176 + randint(-5, 20)

console = 2589, 2055
copy_translate = 2358, 2048  # 截图识别文字后，点击复制
aweme_list_button = x + 70 + randint(-60, 100), y + 520

time_sample = [0.01, 0.021, 0.031, 0.023]
time_1 = 0.1 + choice(time_sample)
time_2 = 0.2 + choice(time_sample)
time_3 = 0.3 + choice(time_sample)
time_4 = 0.4 + choice(time_sample)
time_5 = 0.5 + choice(time_sample)
time_6 = 0.6 + choice(time_sample)
time_7 = 0.7 + choice(time_sample)
time_8 = 0.8 + choice(time_sample)
time_10 = 1.0 + choice(time_sample)
time_13 = 1.3 + choice(time_sample)
time_15 = 1.5 + choice(time_sample)
time_18 = 1.8 + choice(time_sample)
time_20 = 2.0 + choice(time_sample)


def back():
    m.click(x, y)


def sleep(seconds):
    time.sleep(seconds)
    # print(f'时长: {seconds:.2f}s')


def count_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        log.info(f'>>>> {func.__name__} 执行时长：{time.time() - start_time:.2f}s <<<<')
        return result

    return wrapper


def fly_left():
    # 向左滑动
    m.moveTo(right[0], right[1], duration=time_1)
    m.dragTo(left[0] - 300, left[1], duration=time_3)
    # 返回再滑动
    back()
    sleep(time_5)
    m.moveTo(right[0], right[1], duration=time_1)
    m.dragTo(left[0] - 300, left[1], duration=time_3)


def fly_right():
    # 向右滑动
    m.moveTo(left[0], left[1], duration=time_1)
    m.dragTo(right[0] + 300, right[1], duration=time_1)


def head_to_tail():
    """向下滑动，从上到下"""
    new_x = head[0] + randint(-400, 100)
    m.moveTo(new_x, head[1])
    m.dragTo(new_x, tail[1], duration=time_5)


def tail_to_head_aweme():
    """向上滑动，从下到上"""
    new_x = head[0] + randint(-400, 100)
    m.moveTo(new_x, tail[1] + randint(-300, 20))
    m.dragTo(new_x + randint(30, 50), head[1] + randint(-100, -80),
             duration=randint(2, 4) / 46.0)
    # sleep(time_1 + time_10 + randint(1, 5) / 16)
    sleep(time_4 + randint(1, 3) / 30)


def tail_to_head_promotion():
    """向上滑动，从下到上"""
    new_x = head[0] + randint(-400, 100)
    m.moveTo(new_x, tail[1] + randint(-300, 100))
    m.dragTo(new_x + randint(30, 50), head[1] + randint(-100, 100),
             duration=randint(1, 3) / 30.0)
    sleep(time_6 + randint(1, 5) / 30)


def hua(exec_count, hua_method, step=9.0):
    """根据总数控制 hua 划的次数"""
    count = math.ceil(exec_count / float(step)) + 1
    start = time.strftime('%H:%M:%S')
    print(F'开始时间：{start}，初始计数 {count}')
    start = time.time()

    while count > 0:
        if count % 10 == 0 or count == 1:
            print('计数', count, '耗时', f'{time.time() - start:.2f} s')
        count -= 1
        hua_method()


def hua_by_times(exec_times, hua_method):
    """根据滑动次数滑动"""
    count = exec_times
    # print(F'开始时间：{start}，初始计数 {count}')
    start = time.time()
    while count > 0:
        count -= 1
        hua_method()
    print('滑动耗时', f'{time.time() - start:.2f} s')


def click_avatar():
    m.click(avatar[0], avatar[1])
    print('返回再点击，等待2s')
    sleep(time_15 + randint(3, 5) / 20.0)
    back()
    sleep(time_5)
    m.click(avatar[0], avatar[1])


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
    m.moveTo(console[0], console[1], duration=.1)
    m.click(console[0], console[1])


def random_read_aweme():
    m.click(aweme_three[0] + randint(50, 350), aweme_three[1] + randint(-100, 0))
    sleep(time_5)
    m.doubleClick()
    sleep(time_2)
    back()


# 细节控制
def slow_down_in_key_action(duration=.5):
    """在关键节点缓慢操作，比如晚上"""
    sleep(duration)


base_dir = 'D:\\douyin2'
source_base_dir = 'D:\\douyin'


def _check_convert_file_exits(times=20, interval=.3, file_tags='all'):
    """检验转换的文件/源文件是否存在

    :param times: 等待循环次数
    :param interval: 等待间隔
    :param file_tags: 文件标签，默认 all：所有文件
    """
    step_interval = .1
    # 等待源文件出现
    has_source_file = False
    source_files = None
    cur = time.time()
    source_times = times
    while source_times > 0:
        if source_times > 15:
            sleep(step_interval)
            source_times -= 1
        else:
            sleep(interval)
        source_files = os.listdir(source_base_dir)
        if file_tags != 'all':
            source_files = list(filter(lambda x: file_tags in x, source_files))
            if not source_files or len(source_files) < 1:
                source_times -= 1
            else:
                has_source_file = True
                break
    # log.info(f'获取标签为 {file_tags} 的 【源文件】 {source_files} 时长：{time.time() - cur:.2f}s')
    if not has_source_file or source_files is None:
        err = f'没有获取到标签为 {file_tags} 的 【源文件】，请检查'
        log.error(err)
        # 不报错，改为查看内容
        a = input(f'请查看标签为 {file_tags} 的文件是否存在')
        # raise ValueError(err)

    # 转换文件
    # log.info(f'转换标签为 {file_tags} 的文件')
    convert_file(include=file_tags)

    has_convert_file = False
    convert_files = None
    cur = time.time()
    convert_times = times
    while convert_times > 0:
        if convert_times > 15:
            sleep(step_interval)
            convert_times -= 1
        else:
            sleep(interval)
        convert_files = os.listdir(base_dir)
        if file_tags != 'all':
            convert_files = list(filter(lambda x: file_tags in x, convert_files))
        if not convert_files or len(convert_files) == 0:
            convert_times -= 1
        else:
            has_convert_file = True
            break
    # log.info(f'获取标签为 {file_tags} 的【转换文件】{convert_files} 时长：{time.time() - cur:.2f}s')
    if not has_convert_file or convert_files is None:
        log.error(f'没有获取到标签为 {file_tags} 的【解析后文件】，请检查')
        a = input(f'请查看标签为 {file_tags} 的【解析后文件】')
        # raise ValueError('没有获取到【解析后的文件】，请检查 base_dir 中内容')
    return convert_files


@count_time
def get_promotion_count(has_shop_entry):
    """获取商品总数"""
    # 没有商品橱窗，直接返回商品数为0
    if not has_shop_entry:
        return 0
    try:
        files = _check_convert_file_exits(file_tags='promotion')
    except ValueError:
        log.error('解析 商品 文件失败，请检查 base_dir 中的内容')
        return
    if len(files) != 1:
        raise Exception(f"当前有两个商品文件，请检查 {base_dir} 中的内容")
    file_name = os.path.join(base_dir, files[0])
    with open(file_name, encoding='utf-8') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        real_lines = list(filter(lambda x: x, lines))
        last_line = str(real_lines[-1])
        promotion_info = json.loads(last_line)
        count = promotion_info.get('count')

    log.info(f'商品数量为：【{count}】')
    return count


@count_time
def check_user_in_db():
    """验证用户信息相关功能

    如果用户存在在数据库，且有作品信息，则返回 True
    如果用户信息需要更新入库，则返回 False
    """
    log.info('获取用户简单的数据：名称、作品数量')
    user_info = {'flag': True}
    exclude_users = ['pangpang', 'Alliew', '大王叫我来巡山', '"lp":', '啥名', '已重置']
    try:
        files = _check_convert_file_exits(file_tags='user')
    except ValueError as e:
        raise Exception(e)

    for file in files:
        file_name = os.path.join(base_dir, file)
        if os.path.isfile(file_name) and file.startswith('user'):
            line_json = get_last_line_in_file(file_name, exclude=exclude_users)
            user = line_json.get('user')
            if not user or len(user) < 1:
                return user_info
            else:
                nickname = user.get('nickname', '')
                user_info['name'] = user.get('nickname', '')
                uid = user.get('uid')
                user_info['suren_id'] = uid
                user_info['with_fusion_shop_entry'] = user.get('with_fusion_shop_entry')
                user_info['aweme_count'] = user.get('aweme_count')
                aweme_count = user_info['aweme_count']
                commerce_info = user.get('commerce_info')
                user_info['office_info_len'] = len(commerce_info.get('offline_info_list')) \
                    if commerce_info is not None else None
                user_info['enterprise_verify_reason'] = user.get('enterprise_verify_reason')
                user_info['custom_verify'] = user.get('custom_verify')  # 抖音标签，如：好物推荐官
                if int(aweme_count) == 20:
                    # 由于爬取的问题，有些作品数为20的用户全部有问题
                    return user_info
                break
    else:
        return user_info

    # 查询数据库
    db_pool = get_db_tool()
    conn = db_pool.connection()
    cursor = conn.cursor()

    user_sql = """
    SELECT COUNT(a.aweme_id)
FROM douyin_aweme a
WHERE a.suren_id = %s
    """

    if uid is None:
        log.info('获取用户 uid 为空，推荐使用 nickname 查询')
        user_sql = """SELECT u.nickname, u.suren_id, COUNT(a.aweme_id) AS a_num 
    FROM douyin_aweme AS a
           INNER JOIN douyin_user AS u
                      ON u.suren_id = a.suren_id
                        AND u.nickname = %s 
    GROUP BY a.suren_id
    HAVING COUNT(a.aweme_id) > 21
    OR COUNT(a.aweme_id) = %s
    """

    # 对插入用户埋点，根据用户是否入库统计入库比例
    maidian_sql = """INSERT INTO douyin_maidian (suren_id, nickname, is_new, update_time)
VALUES (%s, %s, %s, NOW())
    """
    try:
        # 做两种查询方式的判断
        if uid is None:
            cursor.execute(user_sql, (nickname, int(aweme_count)))
            result = cursor.fetchall()
            if result is None or len(result) < 1:
                log.info(f'用户 {nickname} 在数据库中不存在 or 作品信息不全')
                user_info['flag'] = False
            else:
                log.info(f'\n\t\t用户 {nickname} 有 【{result[0][2]} 作品\n】')
        else:
            cursor.execute(user_sql, (int(uid)))
            result = cursor.fetchone()
            count = result[0]
            if count:
                log.info(f'\n\t\t用户 {uid} - {nickname} 有 【{count} 作品】\n')
            user_info['flag'] = True if count else False
        # 根据flag插入埋点
        cursor.execute(maidian_sql, (str(uid), nickname, not user_info['flag']))
        conn.commit()
    except:
        traceback.print_exc()
        conn.rollback()
    finally:
        cursor.close()
        conn.close()
    log.info(user_info)
    return user_info


def get_last_line_in_file(file_name, exclude=None):
    """获取文件最后一行

    :param file_name: 文件名称
    :param exclude: 排除的内容，如果某一行包括该内容，则排除

    exclude 的主要应用场景是测试用的用户，自身信息带入 user 文件，从而覆盖了最新的内容
    """
    with open(file_name, encoding='utf-8') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        real_lines = list(filter(lambda x: x, lines))
        if exclude is not None and isinstance(exclude, list):
            for item in exclude:
                real_lines = list(filter(lambda x: item not in x, real_lines))
        last_line = str(real_lines[-1])
        line_json = json.loads(last_line)
        # log.info(f'文件的最后一行为：{line_json}')
        return line_json


@count_time
def _fly_up_to_get_all_aweme(aweme_num):
    """向上滑动获取所有作品

    :param aweme_num 作品总数，用户判断滑动次数
    :param return_times 判断返回上一页时，是返回 一次还是两次
    """
    need_return_wait = False
    if aweme_num > 40:
        # 修改为2， 提高执行效率
        hua_by_times(3, tail_to_head_aweme)
    elif aweme_num > 20:
        hua_by_times(2, tail_to_head_aweme)
    else:
        log.info('作品数量小于20')
        need_return_wait = True
    # 由于分析文件内容置后，所以这里的等待时间可以去除
    # 如果直接从作品返回需要等待时间
    if need_return_wait:
        sleep(time_5 + randint(1, 2) / 10.0)
        back()
        sleep(time_8 + randint(1, 2) / 10.0)
    else:
        back()
    # elif return_times == 2:
    #     # 返回两次
    #     back()
    #     print('返回一次')
    #     sleep(time_10)
    #     # 设置随机访问视频
    #     tea = randint(1, 10)
    #     if tea > 8:
    #         log.info('进入查看视频')
    #         random_read_aweme()
    #
    #     # 返回消息列表
    #     back()
    #     print('返回第二次')
    #     sleep(time_10)


def _back_for_times(**kwargs):
    """在判断用户已经入库后，直接根据次数返回"""
    return_times = kwargs.get('return_times')
    for i in range(return_times):
        back()
        sleep(time_3)
        # focus_console()
        # a = input('当前返回需要确认')


def clean_data():
    """清理数据"""
    log.info('清空数据')
    clean_dir(base_dir)
    clean_dir(source_base_dir)


class SurenInfo:
    def __init__(self, return_times, *args, **kwargs):
        self.return_times = return_times

        log.info('获取素人信息')

        self._user_info = check_user_in_db()
        # 判断用户是否已经在数据库中，且包含作品信息
        # 注意：在 check_user_in_db() 方法中，返回的flag=True，
        #   表示用户在数据库中，取反则意味着不是新用户，故逻辑上要加 not
        self._new_user_flag = not self._user_info.get('flag')
        if self.return_depends_on_flag():
            self.more_detail()
        pass

    def return_depends_on_flag(self):
        """根据 flag 判断下一步操作

        如果用户是新用户，则进一步获取数据；
        否则，直接返回消息列表

        :return has_next: 判断下一步操作，
                          True：进入用户橱窗和作品操作
                          False：意味着需要直接返回，该操作在内容中有实现
        """
        has_next = False
        global multiple_return_times
        if self._new_user_flag:
            multiple_return_times = 0
            has_next = True
        else:
            multiple_return_times += 1
            # 如果同时有多个已经入库的用户，那么会一直点击用户，然会返回
            # 这样的操作发生过于频繁会被封锁获取用户的接口
            if multiple_return_times > 2:
                log.info('已经连续返回超过3次了，接下来全部滑动作品2次，直到获取新用户为止')
                hua_by_times(2, tail_to_head_aweme)
            log.info('用户已经在数据库中存在，返回消息列表')
            _back_for_times(return_times=self.return_times)
            clean_data()
        return has_next

    def _back_in_times(self):
        """在判断用户已经入库后，直接根据次数返回"""
        for i in range(self.return_times):
            back()
            sleep(time_3)

    def more_detail(self):
        """获取更多的内容，如橱窗、作品"""
        self.promotion_info()

    def promotion_info(self):
        """橱窗信息"""
        # 判断是否有商品橱窗
        # focus_console()
        # has_aweme = int(input('>>> 获取 橱窗 1 or 作品 2 or 返回 0：'))
        has_shop_entry = self._user_info.get('with_fusion_shop_entry')  # 是否有橱窗
        if has_shop_entry is None:
            log.info('获取橱窗失败')
            focus_console()
            has_shop_entry = int(input('>>> 获取 橱窗 1 or 作品 2 or 返回 0：'))
        else:
            has_shop_entry = True if has_shop_entry in ['true', 'True', 'True', True] else False
        self._has_shop_entry = has_shop_entry

        # title栏，如果以下内容存在，橱窗位置会往下移动
        enterprise_verify_reason = self._user_info.get('enterprise_verify_reason')  # 官方认证
        office_info_len = self._user_info.get('office_info_len')  # 官方信息
        custom_verify = self._user_info.get('custom_verify')  # 抖音好物推荐官

        if has_shop_entry:
            # 点击橱窗
            # focus_console()
            aweme_x, aweme_y = aweme_list_button[0], aweme_list_button[1]
            y_rand = randint(-6, 6)
            hold_time = .1
            log.info('点击橱窗，获取商品')
            # 默认位置
            if not enterprise_verify_reason and not office_info_len and not custom_verify:
                m.click(aweme_x, aweme_y + 12 + y_rand, duration=hold_time)
            if enterprise_verify_reason and not office_info_len:
                # 如果有企业认证，添加 y值88
                m.click(aweme_x, aweme_y + 88 + y_rand, duration=hold_time)
            if office_info_len:
                m.click(aweme_x, aweme_y + 136 + y_rand, duration=hold_time)
            if custom_verify:
                m.click(aweme_x, aweme_y + 63 + y_rand, duration=hold_time)
            # click_or_not = int(input('>>> 橱窗 调整 1 or 不调整 0 '))
            # to_x, to_y = m.position()
            # m.click(to_x, to_y)
            sleep(time_5)

            # 获取商品总数
            promotion_count = get_promotion_count(has_shop_entry)
            if promotion_count is None and has_shop_entry:
                log.info('获取商品总数失败')
                focus_console()
                promotion_count = int(input('>>> 商品总数: '))
            else:
                promotion_count = int(promotion_count)

            if promotion_count > 300:
                log.info('用户商品橱窗数量大于 300，只取前 300 商品')
                promotion_count = 300
            if promotion_count > 20:
                hua(promotion_count, tail_to_head_promotion, step=20)
            # 返回作品界面
            back()
            # sleep(time_3)
            # 解析文件放在这一步，防止没有获取商品信息而报错
            _check_convert_file_exits(file_tags='promotion')
        else:
            log.info("用户没有橱窗信息")

    def aweme_info(self):
        """获取作品信息"""
        aweme_count = self._user_info.get('aweme_count')
        if aweme_count is None:
            log.info('没有获取作品数量')
            m.click(console[0], console[1])
            aweme_count = int(input('>>> 请输入作品总数：'))
        else:
            aweme_count = int(aweme_count)

        if aweme_count:
            # 作品向上滑动
            log.info(f'作品数量为 【{aweme_count}】')
            if not self._has_shop_entry and aweme_count > 20:
                log.info(f'因为没有橱窗信息，且作品数量超过20，作品只获取30个')
                aweme_count = 30
            _fly_up_to_get_all_aweme(aweme_count)
            _check_convert_file_exits(file_tags='zuopin')
        else:
            log.info(f'用户 {self._user_info["name"]}')
            for i in range(self.return_times):
                back()
                if i == 0:
                    sleep(time_3)


@count_time
def get_suren_info(*args, **kwargs):
    """获取素人信息，判断是否有橱窗

    有则获取橱窗信息和作品信息
    """
    return_times = kwargs.get('return_times')
    if return_times is None:
        log.error('返回次数必须给定')
        raise Exception('返回次数必须输入')
    suren_info = SurenInfo(return_times=return_times)


def roll_page():
    m.moveTo(head[0], head[1], duration=time_1)
    m.dragTo(tail[0], tail[1] + 50, duration=time_1)


@count_time
def fetch_user(flag_num, fetch_method, **kwargs):
    """点击第三个用户，获取信息"""
    chose_third = randint(1, 10)
    click_title_or_aweme_third = chose_third > flag_num
    return_times_third = 2 if click_title_or_aweme_third else 1
    if click_title_or_aweme_third:
        log.info('点击头像进入视频后，再进入主页')
        m.click(aweme_three[0], aweme_three[1], duration=.2 + random() / 20.0)
        sleep(time_18)
        # fly_left()  # 向左滑动，进入主页
        click_avatar()  # 点击头像，进入主页
    else:
        log.info('直接进入主页')
        m.click(aweme_three[0], aweme_three[1] - 160 + randint(-20, 10))
        sleep(time_5)
        if kwargs.get('night'):
            # 晚上延迟
            slow_down_in_key_action(duration=time_8)
    # 执行滑动判断逻辑
    get_suren_info(return_times=return_times_third, **kwargs)


@count_time
def delete_user_in_message():
    """删除最下面一个用户信息，前提是已经读取过该用户信息"""
    convertX, convertY = 65536 * aweme_three[0] // 3840 + 1, 65536 * aweme_three[1] // 2160 + 1
    ctypes.windll.user32.SetCursorPos(aweme_three[0], aweme_three[1])
    ctypes.windll.user32.mouse_event(2, convertX, convertY, 0, 0)
    sleep(0.95)
    ctypes.windll.user32.mouse_event(4, convertX, convertY, 0, 0)

    # m.moveTo(delete_x, delete_y, duration=.1)
    m.click(delete_x, delete_y)
    log.info('删除消息列表中数据')
    sleep(time_5)


def _before_action():
    """执行前清理文件，避免造成数据异常、缺失"""
    # 清理数据
    if os.listdir(base_dir):
        clean_dir(base_dir)
    if os.listdir(source_base_dir):
        clean_dir(source_base_dir)


def action(fetch_method, **kwargs):
    """只获取所有作品信息"""
    _before_action()
    flag_num = 11

    start = time.time()
    log.info('=' * 50)
    # 点击第三个视频
    fetch_user(flag_num, get_suren_info, **kwargs)
    # 数据入库
    log.info('存入数据库')
    handle_file(os.listdir(base_dir))
    # 清理数据
    clean_dir(base_dir)
    clean_dir(source_base_dir)
    # 删除小写列表中数据
    delete_user_in_message()
    execute_time = time.time() - start
    if execute_time > 60:
        execute_minute = int(execute_time // 60)
        execute_seconds = execute_time % 60
        log.info(f'总执行时长：{execute_minute} m {execute_seconds:.2f} s')
    else:
        log.info(f'总执行时长：{time.time() - start:.2f} s')
    log.info('=' * 50 + '\n')


if __name__ == '__main__':
    user_nums = 0
    roll_times = 0
    multiple_return_times = 0
    now = datetime.datetime.now()
    is_night = now.hour > 17 and now.minute > 30
    while True:
        roll_times += 1
        if roll_times < 2:
            # get_suren_info(1)
            action(get_suren_info, night=is_night)  # 执行步骤二，已经融合了执行步骤一 @2109-11-22
            sleep(time_8)
            user_nums += 1
            print(f'已经获取 {user_nums} 个用户')
        else:
            focus_console()
            is_continue = int(input('>>> 是否继续：'))
            if is_continue:
                roll_times = 0
                #         # m.hotkey('alt', 'tab')
                #         # roll_page()
                #         # roll_times += 1
                #         # log.info(f'翻页次数 {roll_times}')
                #         # action() # 执行步骤一
                action(get_suren_info, night=is_night)  # 执行步骤二，已经融合了执行步骤一 @2109-11-22
                user_nums += 1
                print(f'已经获取 {user_nums} 个用户')
            else:
                break

    # m.hotkey('alt', 'tab')
    # # draw_cycle()
    # if is_continue:
    #     m.hotkey('ctrl', 'F5')
    # print('ctrl+f2 停止')
