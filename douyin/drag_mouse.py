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
from random import random, randrange, sample, choice, randint

import pyautogui as m

from douyin.conver_encoding import convert_file, clean_dir
from douyin.extract_promotion_detail import handle_file
from tools import logger
from tools.parser_config import get_db_tool

width, height = m.size()

# m.moveTo(300, 300, duration=.25)

log = logger.logger


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
aweme_list_button = x + 70, y + 515

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


def fly_left():
    # 向左滑动
    m.moveTo(right[0], right[1], duration=time_1)
    m.dragTo(left[0] - 300, left[1], duration=time_3)
    # 返回再滑动
    back()
    time.sleep(time_5)
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
             duration=randint(1, 3) / 26.0)
    time.sleep(time_2 + time_15 + randint(1, 10) / 15)


def tail_to_head_faster():
    """向上滑动，从下到上"""
    new_x = head[0] + randint(-400, 100)
    m.moveTo(new_x, tail[1] + randint(-300, 20))
    m.dragTo(new_x + randint(30, 50), head[1] + randint(-100, -80),
             duration=randint(1, 3) / 25.0)
    time.sleep(time_1 + randint(1, 10) / 15)


def hua(exec_count, hua_method, step=9):
    """控制 hua 划的次数"""
    print(time.strftime('%H:%M:%S'))
    count = math.ceil(exec_count / step) + 1

    while count > 0:
        print('计数', count)
        count -= 1
        hua_method()


def click_avatar():
    m.click(avatar[0], avatar[1])
    print('返回再点击，等待2s')
    time.sleep(2 + randint(3, 5) / 20.0)
    back()
    time.sleep(time_5)
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
    time.sleep(time_5)
    m.doubleClick()
    time.sleep(time_2)
    back()


lock = threading.RLock()


def _write_to_new_file(filename, new_filename):
    """去除空行，写入新文件"""
    id = threading.currentThread().getName()
    lock.acquire()

    file1 = open(filename, 'rt', encoding='utf-8')
    file2 = open(new_filename, 'wt', encoding='utf-8')
    try:
        for line in file1:
            new_line = line.strip()
            if new_line:  # 空行不插入
                file2.write(line)
    finally:
        file1.close()
        file2.close()
    lock.release()
    print(f"Thead {id} exit")


def _read_from_new_file(new_filename):
    """从新文件中读取内容"""
    # id = threading.currentThread().getName()
    # lock.acquire()
    with open(new_filename, 'rb') as f:
        # off = -50
        # while True:
        # f.seek(off, 2)
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        last_line = str(lines[-1].decode('utf-8'))
        # if len(lines) >= 2:
        #     break
        # else:
        #     off *= 2
    # lock.release()
    # print(f'Thread {id} exit')
    return last_line


def check_user_in_db():
    """验证用户信息相关功能

    如果用户存在在数据库，且有作品信息，则返回False
    如果用户信息需要更新入库，则返回True
    """
    user_info = {'flag': True}
    convert_file()
    base_dir = 'd:\\douyin2'
    time.sleep(.8)
    files = os.listdir(base_dir)
    nickname = None
    with_fusion_shop_entry = None
    aweme_count = None

    if not files or len(files) == 0:
        log.error('没有获取到文件，请检查')
        raise Exception('没有获取到解析后的文件，请检查 base_dir 中内容')

    for file in files:
        file_name = os.path.join(base_dir, file)
        if os.path.isfile(file_name) and file.startswith('user') and '_' in file:
            line = get_last_line_in_file(file_name)
            nickname = re.findall(r'"nickname":"(.*?)"', line)
            print('=' * 20)
            if nickname is None or len(nickname) < 1:
                print(f'作者名称{nickname}')
                return user_info
            else:
                user_info['name'] = nickname[0]
                user_info['with_fusion_shop_entry'] = re.findall(
                    r'"with_fusion_shop_entry":(.*?),', line)[0]
                user_info['aweme_count'] = re.findall(r'"aweme_count":(\d+)', line)[0]
                break
    for file in files:
        file_name = os.path.join(base_dir, file)
        if os.path.isfile(file_name) and 'promotion' in file_name:
            with open(file_name, encoding='utf-8') as f:
                lines = f.readlines()
                lines = [line.strip() for line in lines]
                real_lines = list(filter(lambda x: x, lines))
                last_line = str(real_lines[-1])
                promotion_info = json.loads(last_line)
                count = promotion_info.get('count')
                user_info['promotion_count'] = count
                break

    # 查询数据库
    db_pool = get_db_tool()
    conn = db_pool.connection()
    cursor = conn.cursor()
    sql = """SELECT u.nickname, u.suren_id, COUNT(a.aweme_id) AS a_num 
FROM douyin_aweme AS a
       INNER JOIN douyin_user AS u
                  ON u.suren_id = a.suren_id
                    AND u.nickname = %s 
GROUP BY a.suren_id
HAVING COUNT(a.aweme_id) > 21
"""
    try:
        cursor.execute(sql, nickname)
        result = cursor.fetchall()
        if not result or len(result) < 1:
            log.info(f'用户 {nickname} 不在数据库中')
            flag = False
        else:
            log.info(f'用户 {nickname} 有 {result[0][2]} 作品')
    except:
        traceback.print_exc()
        conn.rollback()
    finally:
        cursor.close()
        conn.close()
    return user_info


def get_last_line_in_file(file_name):
    """获取文件最后一行"""
    # 去除空行
    new_filename = file_name.replace('_', '-')

    threading.Thread(target=_write_to_new_file, args=(file_name, new_filename)).start()

    # _write_to_new_file(file_name, new_filename)
    time.sleep(.5)
    last_line = _read_from_new_file(new_filename)

    # 删除旧文件
    # os.remove(file_name)
    # 数据量每次都很小，没必要删除，不然容易有异常

    return last_line


def fly_up_to_get_all_aweme(return_times=1):
    """向上滑动获取所有作品

    :param return_times 判断返回上一页时，是返回 一次还是两次
    """
    m.moveTo(console[0], console[1])
    m.click(console[0], console[1])
    aweme_num = int(input('>>> 请输入作品总数：'))
    if aweme_num > 20:
        hua(aweme_num, tail_to_head, step=7)
    if return_times == 1:
        # 返回一次
        back()
        time.sleep(time_8 + randint(1, 2) / 10.0)
    elif return_times == 2:
        # 返回两次
        back()
        time.sleep(time_10)
        # 设置随机访问视频
        tea = randint(1, 10)
        if tea > 8:
            log.info('进入查看视频')
            random_read_aweme()

        # 返回消息列表
        back()
        time.sleep(time_10)


def _back_for_times(return_times):
    """根据次数返回"""
    for i in range(return_times):
        back()
        time.sleep(time_10)


def get_suren_info(*args, **kwargs):
    """获取素人信息，判断是否有橱窗

    有则获取橱窗信息和作品信息
    """
    return_times = kwargs.get('return_times')
    if return_times is None:
        log.error('返回次数必须给定')
        raise Exception('返回次数必须输入')
    source_base_dir = 'D:\\douyin'
    base_dir = 'D:\\douyin2'
    time.sleep(.5)
    # 判断用户是否已经在数据库中，且包含作品信息
    if check_user_in_db():
        log.info('用户已经在数据库中存在，返回消息列表')
        _back_for_times(return_times)
        # 清理数据
        clean_dir(base_dir)
        clean_dir(source_base_dir)
        return
    # 判断是否有商品橱窗
    focus_console()
    has_aweme = int(input('>>> 获取 橱窗 1 or 作品 2 or 返回 0：'))
    if has_aweme == 1:
        # 点击橱窗
        m.moveTo(aweme_list_button[0], aweme_list_button[1])
        click_or_not = int(input('>>> 是否自由点击橱窗: '))
        if click_or_not:
            log.info('点击完成？')
            focus_console()
        else:
            to_x, to_y = m.position()
            m.click(to_x, to_y)
        time.sleep(time_5)
        focus_console()
        promotion_amount = int(input('>>> 商品总数: '))
        if promotion_amount > 10:
            hua(promotion_amount, tail_to_head_faster, step=8)
        # 返回作品界面
        back()
        time.sleep(time_4)
    if has_aweme:
        # 作品向上滑动
        fly_up_to_get_all_aweme(return_times)

        convert_file(exclude_file='user')
        # 存储数据入库
        log.info('存入数据库')
        handle_file(os.listdir(base_dir))
        # 清理数据
        clean_dir(base_dir)
        clean_dir(source_base_dir)
    else:
        for i in range(return_times):
            back()
            time.sleep(time_10)


def roll_page():
    m.moveTo(head[0], head[1], duration=time_1)
    m.dragTo(tail[0], tail[1] + 50, duration=time_1)


def action():
    """流程"""
    # 点击第一个视频
    chose_first = randint(1, 10)
    if chose_first > 11:  # 如果点击被封了，就走下面的逻辑
        m.click(aweme_one[0], aweme_one[1], duration=time_1)
    else:
        m.moveTo(aweme_one[0], aweme_one[1] - 200)
        move_first = input('>>> 是否需要移动到第一个视频：')
        if move_first:
            first_x, first_y = m.position()
            m.click(first_x, first_y)
        else:
            m.click(aweme_one[0], aweme_one[1] - 200)

    time.sleep(time_20 + time_3)
    fly_left()  # 向左滑动，进入主页 tip：可能不需要这步骤
    get_suren_info()
    # 点击第二个视频
    m.click(aweme_two[0], aweme_two[1], duration=0.2 + random() / 3.0)
    get_suren_info()
    m.click(aweme_three[0], aweme_three[1], duration=.2 + random() / 2.0)
    get_suren_info()
    # time.sleep(time_10)


def fetch_first_user(flag_num, fetch_method):
    """点击第一个用户，获取信息"""
    chose_first = randint(1, 10)
    click_title_or_aweme = chose_first > flag_num
    return_times = 2 if click_title_or_aweme else 1
    if click_title_or_aweme:  # todo: 如果点击被封了，就走下面的逻辑
        log.info('点击头像进入视频后，再进入主页')
        m.click(aweme_one[0], aweme_one[1], duration=time_1)
        time.sleep(time_20 + time_3)
        # fly_left()  # 向左滑动，进入主页
        click_avatar()  # 点击头像，进入主页
    else:
        log.info('直接进入主页')
        focus_console()
        m.moveTo(aweme_one[0], aweme_one[1] - 200)
        move_first = input('>>> 移动到第一个视频：')
        if move_first:
            first_x, first_y = m.position()
            m.click(first_x, first_y)
        else:
            m.click(aweme_one[0], aweme_one[1] - 200)
    # 选择执行的功能
    fetch_method(return_times=return_times)


def fetch_second_user(flag_num, fetch_method):
    """点击第二个用户，获取信息"""
    chose_second = randint(1, 10)
    click_title_or_aweme_second = chose_second > flag_num
    return_times_second = 2 if click_title_or_aweme_second else 1
    if click_title_or_aweme_second:
        log.info('点击头像进入视频后，再进入主页')
        m.click(aweme_two[0], aweme_two[1], duration=0.2 + random() / 3.0)
        time.sleep(time_20 + time_3)
        click_avatar()  # 点击头像，进入主页
    else:
        log.info('直接进入主页')
        focus_console()
        m.moveTo(aweme_two[0] + 30 + randint(3, 8), aweme_two[1] - 103)
        move_second = input('>>> 移动到第二个视频：')
        if move_second:
            second_x, second_y = m.position()
            m.click(second_x, second_y)
        else:
            m.click(aweme_two[0] + 30 + randint(3, 8), aweme_two[1] - 103)
    # 执行滑动判断逻辑
    fetch_method(return_times=return_times_second)


def fetch_third_user(flag_num, fetch_method):
    """点击第三个用户，获取信息"""
    chose_third = randint(1, 10)
    click_title_or_aweme_third = chose_third > flag_num
    return_times_third = 2 if click_title_or_aweme_third else 1
    if click_title_or_aweme_third:
        log.info('点击头像进入视频后，再进入主页')
        m.click(aweme_three[0], aweme_three[1], duration=.2 + random() / 2.0)
        time.sleep(time_20 + time_3)
        # fly_left()  # 向左滑动，进入主页
        click_avatar()  # 点击头像，进入主页
    else:
        log.info('直接进入主页')
        focus_console()
        m.moveTo(aweme_three[0], aweme_three[1] - 150)
        # move_third = input('>>> 移动到第三个视频：')
        # if move_third:
        third_x, third_y = m.position()
        m.click(third_x, third_y, duration=.3)
        # else:
        #     m.click(aweme_three[0], aweme_three[1] - 150)
    # 执行滑动判断逻辑
    fetch_method(return_times=return_times_third)


def delete_user_in_message():
    """删除最下面一个用户信息，前提是已经读取过该用户信息"""
    time.sleep(.3)
    convertX, convertY = 65536 * aweme_three[0] // 3840 + 1, 65536 * aweme_three[1] // 2160 + 1
    ctypes.windll.user32.SetCursorPos(aweme_three[0], aweme_three[1])
    ctypes.windll.user32.mouse_event(2, convertX, convertY, 0, 0)
    time.sleep(0.8)
    ctypes.windll.user32.mouse_event(4, convertX, convertY, 0, 0)

    m.moveTo(delete_x, delete_y, duration=.1)
    m.click(delete_x, delete_y)


def action_two(fetch_method):
    """只获取所有作品信息"""
    flag_num = 8

    # 点击第三个视频
    fetch_third_user(flag_num, fetch_method)
    delete_user_in_message()
    # 点击第二个视频
    # fetch_second_user(flag_num, fetch_method)
    # 点击第一个视频
    # fetch_first_user(flag_num, fetch_method)


if __name__ == '__main__':
    # roll_times = 0
    while True:
        action_two(get_suren_info)  # 执行步骤二，已经融合了执行步骤一 @2109-11-22
    #     focus_console()
    #     is_continue = int(input('>>> 是否继续：'))
    #     if is_continue:
    #         # m.hotkey('alt', 'tab')
    #         # roll_page()
    #         # roll_times += 1
    #         # log.info(f'翻页次数 {roll_times}')
    #         # action() # 执行步骤一
    #         action_two(get_suren_info)  # 执行步骤二，已经融合了执行步骤一 @2109-11-22
    #     else:
    #         break

    # m.hotkey('alt', 'tab')
    # # draw_cycle()
    # if is_continue:
    #     m.hotkey('ctrl', 'F5')
    # print('ctrl+f2 停止')
