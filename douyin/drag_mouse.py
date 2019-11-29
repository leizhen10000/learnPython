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
aweme_three = x + 135 + randint(-60, 190), y + 1400
right = x + 800 + randrange(0, 50, 3), y + 300 + randrange(0, 1200, 3)
left = x + 100 + randrange(0, 50, 3), right[1] + randrange(0, 10, 2)
avatar = x + 976 + randint(-3, 3), y + 987 + randint(-3, 3)
delete_x, delete_y = x + 483 + randint(-80, 70), y + 1129 + randint(-5, 20)

console = 2589, 2055
copy_translate = 2358, 2048  # 截图识别文字后，点击复制
aweme_list_button = x + 70, y + 520

time_sample = [0.01, 0.021, 0.031, 0.023]
time_1 = 0.1 + choice(time_sample)
time_2 = 0.2 + choice(time_sample)
time_3 = 0.3 + choice(time_sample)
time_4 = 0.4 + choice(time_sample)
time_5 = 0.5 + choice(time_sample)
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
        log.debug(f'--- {func.__name__} 执行时长：{time.time() - start_time:.2f}s ---')
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


def tail_to_head():
    """向上滑动，从下到上"""
    new_x = head[0] + randint(-400, 100)
    m.moveTo(new_x, tail[1] + randint(-300, 20))
    m.dragTo(new_x + randint(30, 50), head[1] + randint(-100, -80),
             duration=randint(2, 4) / 46.0)
    sleep(time_2 + time_10 + randint(1, 5) / 16)


def tail_to_head_faster():
    """向上滑动，从下到上"""
    new_x = head[0] + randint(-400, 100)
    m.moveTo(new_x, tail[1] + randint(-300, 20))
    m.dragTo(new_x + randint(30, 50), head[1] + randint(-100, -80),
             duration=randint(1, 3) / 45.0)
    sleep(time_1 + randint(1, 10) / 15)


def hua(exec_count, hua_method, step=9.0):
    """控制 hua 划的次数"""
    print(time.strftime('%H:%M:%S'))
    count = math.ceil(exec_count / float(step)) + 1

    while count > 0:
        if count % 5 == 1 or count < 10:
            print('计数', count)
        count -= 1
        hua_method()


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


base_dir = 'D:\\douyin2'
source_base_dir = 'D:\\douyin'


@count_time
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
    log.info(f'获取标签为 {file_tags} 的 【源文件】 {source_files} 时长：{time.time() - cur:.2f}s')
    if not has_source_file or source_files is None:
        err = f'没有获取到标签为 {file_tags} 的 【源文件】，请检查'
        log.error(err)
        raise ValueError(err)

    # 转换文件
    log.info(f'转换标签为 {file_tags} 的文件')
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
    log.info(f'获取标签为 {file_tags} 的【转换文件】{convert_files} 时长：{time.time() - cur:.2f}s')
    if not has_convert_file or convert_files is None:
        log.error(f'没有获取到标签为 {file_tags} 的【解析后文件】，请检查')
        raise ValueError('没有获取到【解析后的文件】，请检查 base_dir 中内容')
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

    如果用户存在在数据库，且有作品信息，则返回False
    如果用户信息需要更新入库，则返回True
    """
    log.info('获取用户简单的数据：名称、作品数量')
    user_info = {'flag': True}
    exclude_users = ['pangpang', 'Alliew']
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
                user_info['with_fusion_shop_entry'] = user.get('with_fusion_shop_entry')
                user_info['aweme_count'] = user.get('aweme_count')
                uid = user.get('uid')
                aweme_count = user_info['aweme_count']
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
    try:
        # 做两种查询方式的判断
        if uid is None:
            cursor.execute(user_sql, (nickname, int(aweme_count)))
            result = cursor.fetchall()
            if result is None or len(result) < 1:
                log.info(f'用户 {nickname} 在数据库中不存在 or 作品信息不全')
                user_info['flag'] = False
            else:
                log.info(f'\n用户 {nickname} 有 {result[0][2]} 作品\n')
        else:
            cursor.execute(user_sql, (int(uid)))
            result = cursor.fetchone()
            count = result[0]
            log.info(f'\n用户 {uid} - {nickname} 有 {count} 作品\n')
            user_info['flag'] = True if count else False
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
                log.info(f'排除包含 {exclude} 的行')
                real_lines = list(filter(lambda x: item not in x, real_lines))
        last_line = str(real_lines[-1])
        line_json = json.loads(last_line)
        log.info(f'文件的最后一行为：{line_json}')
        return line_json


@count_time
def fly_up_to_get_all_aweme(aweme_num, return_times=1):
    """向上滑动获取所有作品

    :param aweme_num 作品总数，用户判断滑动次数
    :param return_times 判断返回上一页时，是返回 一次还是两次
    """
    if aweme_num > 200:
        focus_console()
        aweme_num = int(input(f'当前作品数量超过200，请确认数值'))
    base_step = 6  # 如果作品数量少，可以步长大一点
    if 150 > aweme_num > 20:
        hua(aweme_num, tail_to_head, step=base_step)
    elif aweme_num > 150:
        hua(aweme_num, tail_to_head, step=base_step - 0)
    else:
        log.info('作品数量小于20')
    if return_times == 1:
        # 返回一次
        back()
        sleep(time_8 + randint(1, 2) / 10.0)
    elif return_times == 2:
        # 返回两次
        back()
        sleep(time_10)
        # 设置随机访问视频
        tea = randint(1, 10)
        if tea > 8:
            log.info('进入查看视频')
            random_read_aweme()

        # 返回消息列表
        back()
        sleep(time_10)


@count_time
def _back_for_times(return_times):
    """根据次数返回"""
    for i in range(return_times):
        back()
        sleep(time_8)


@count_time
def get_suren_info(*args, **kwargs):
    """获取素人信息，判断是否有橱窗

    有则获取橱窗信息和作品信息
    """
    return_times = kwargs.get('return_times')
    if return_times is None:
        log.error('返回次数必须给定')
        raise Exception('返回次数必须输入')
    # sleep(.1)
    log.info('获取素人信息')
    # 判断用户是否已经在数据库中，且包含作品信息
    user_info = check_user_in_db()
    flag = user_info.get('flag')
    if flag:
        log.info('用户已经在数据库中存在，返回消息列表')
        _back_for_times(return_times)
        # 清理数据
        clean_dir(base_dir)
        clean_dir(source_base_dir)
        return

    # 判断是否有商品橱窗
    # focus_console()
    # has_aweme = int(input('>>> 获取 橱窗 1 or 作品 2 or 返回 0：'))
    has_shop_entry = user_info.get('with_fusion_shop_entry')  # 是否有橱窗
    if has_shop_entry is None:
        log.info('获取橱窗失败')
        focus_console()
        has_shop_entry = int(input('>>> 获取 橱窗 1 or 作品 2 or 返回 0：'))
    else:
        has_shop_entry = True if has_shop_entry in ['true', 'True', 'True', True] else False

    if has_shop_entry:
        # 点击橱窗
        focus_console()
        m.moveTo(aweme_list_button[0], aweme_list_button[1])
        click_or_not = int(input('>>> 橱窗 调整 1 or 不调整 0 '))
        to_x, to_y = m.position()
        m.click(to_x, to_y)
        sleep(time_5)

        # 获取商品总数
        promotion_count = get_promotion_count(has_shop_entry)
        if promotion_count is None and has_shop_entry:
            log.info('获取商品总数失败')
            focus_console()
            promotion_count = int(input('>>> 商品总数: '))
        else:
            promotion_count = int(promotion_count)

        if promotion_count > 20:
            hua(promotion_count, tail_to_head_faster, step=8)
        # 返回作品界面
        back()
        sleep(time_4)
    else:
        log.info("用户没有橱窗信息")

    # 获取作品信息
    aweme_count = user_info.get('aweme_count')
    if aweme_count is None:
        log.info('没有获取作品数量')
        m.click(console[0], console[1])
        aweme_count = int(input('>>> 请输入作品总数：'))
    else:
        aweme_count = int(aweme_count)

    if has_shop_entry or aweme_count:
        # 作品向上滑动
        fly_up_to_get_all_aweme(aweme_count, return_times)
        log.info(f'作品数量为 【{aweme_count}】')

        _check_convert_file_exits(file_tags='zuopin')
        _check_convert_file_exits(file_tags='promotion')
        # 存储数据入库
        log.info('存入数据库')
        handle_file(os.listdir(base_dir))
        # 清理数据
        clean_dir(base_dir)
        clean_dir(source_base_dir)
    else:
        log.info(f'用户 {user_info["name"]}')
        for i in range(return_times):
            back()
            sleep(time_10)


def roll_page():
    m.moveTo(head[0], head[1], duration=time_1)
    m.dragTo(tail[0], tail[1] + 50, duration=time_1)


@count_time
def fetch_user(flag_num, fetch_method):
    """点击第三个用户，获取信息"""
    chose_third = randint(1, 10)
    click_title_or_aweme_third = chose_third > flag_num
    return_times_third = 2 if click_title_or_aweme_third else 1
    if click_title_or_aweme_third:
        log.info('点击头像进入视频后，再进入主页')
        m.click(aweme_three[0], aweme_three[1], duration=.2 + random() / 20.0)
        sleep(time_15 + time_3)
        # fly_left()  # 向左滑动，进入主页
        click_avatar()  # 点击头像，进入主页
    else:
        log.info('直接进入主页')
        # focus_console()
        # m.moveTo(aweme_three[0], aweme_three[1] - 150, duration=.2)
        # move_third = input('>>> 移动到第三个视频：')
        # if move_third:
        # third_x, third_y = m.position()
        m.click(aweme_three[0], aweme_three[1] - 150 + randint(-20, 15))
        sleep(time_5)  # 晚上延迟
        # else:
        #     m.click(aweme_three[0], aweme_three[1] - 150)
    # 执行滑动判断逻辑
    fetch_method(return_times=return_times_third)


@count_time
def delete_user_in_message():
    """删除最下面一个用户信息，前提是已经读取过该用户信息"""
    convertX, convertY = 65536 * aweme_three[0] // 3840 + 1, 65536 * aweme_three[1] // 2160 + 1
    ctypes.windll.user32.SetCursorPos(aweme_three[0], aweme_three[1])
    ctypes.windll.user32.mouse_event(2, convertX, convertY, 0, 0)
    sleep(0.8)
    ctypes.windll.user32.mouse_event(4, convertX, convertY, 0, 0)

    m.moveTo(delete_x, delete_y, duration=.1)
    m.click(delete_x, delete_y)
    log.info('删除消息列表中数据')


def action(fetch_method):
    """只获取所有作品信息"""
    flag_num = 8

    start = time.time()
    log.info('\n' + '=' * 50)
    # 点击第三个视频
    fetch_user(flag_num, fetch_method)
    delete_user_in_message()
    execute_time = time.time() - start
    if execute_time > 60:
        execute_minute = int(execute_time // 60)
        execute_seconds = execute_time % 60
        log.info(f'执行时长：{execute_minute} m {execute_seconds:.2f} s')
    else:
        log.info(f'执行时长：{time.time() - start:.2f}')
    log.info('=' * 50 + '\n')
    # 点击第二个视频
    # fetch_second_user(flag_num, fetch_method)
    # 点击第一个视频
    # fetch_first_user(flag_num, fetch_method)


if __name__ == '__main__':
    roll_times = 0
    while True:
        roll_times += 1
        if roll_times < 1:
            # get_suren_info(1)
            action(get_suren_info)  # 执行步骤二，已经融合了执行步骤一 @2109-11-22
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
                action(get_suren_info)  # 执行步骤二，已经融合了执行步骤一 @2109-11-22
            else:
                break

    # m.hotkey('alt', 'tab')
    # # draw_cycle()
    # if is_continue:
    #     m.hotkey('ctrl', 'F5')
    # print('ctrl+f2 停止')
