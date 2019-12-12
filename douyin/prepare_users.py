#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
# @Time    : 19/12/7 16:05
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @Site    : http://www.leizhen.com
# @File    : prepare_users.py
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
import os
import re
import traceback
from collections import namedtuple, defaultdict

from douyin.conver_encoding import convert_file, clean_dir
from douyin.drag_mouse import check_convert_file_exits
from tools.parser_config import get_db_tool

file_base_dir = 'd:\\douyin2'


def get_user_file_name():
    """获取用户列表所在文件"""
    check_convert_file_exits(file_tags='user')
    file_names = os.listdir(file_base_dir)
    if len(file_names) != 1:
        raise Exception('当前user文件不止一个，请检查问题')
    return os.path.join(file_base_dir, file_names[0])


def extract_user_from_file(user_file):
    """从文件中获取用户"""
    with open(user_file, encoding='utf-8') as f:
        for line in f:
            uid_match = re.search(r'"uid":"(\d+)"', line)
            name_match = re.search(r'"nickname":"(.*?)"', line)
            if uid_match:
                uid = uid_match.group(1)
                name = name_match.group(1)
                yield uid, name


def get_user_in_db_by_uid(uid):
    """根据 uid 获取用户信息

    @:return in_db: 用户在数据库：True，不在数据库：False
    """
    in_db = False
    db_pool = get_db_tool()
    conn = db_pool.connection()
    cursor = conn.cursor()

    sql = "SELECT nickname FROM douyin_user WHERE suren_id = %s"

    try:
        cursor.execute(sql, int(uid))
        data = cursor.fetchall()
        if data is not None and len(data) > 0:
            in_db = True
    except:
        traceback.print_exc()
        conn.rollback()
    finally:
        cursor.close()
        conn.close()
    return in_db


def generate_query_result(user_list):
    """生成查询的结果"""
    User = namedtuple('User', 'uid,nickname,in_db')
    uid_times = defaultdict(int)
    for user in user_list:
        if user[1] in ['Alliew', 'lp', 'pangpang', '大王叫我来巡山', '啥名', '捕梦']:
            continue
        uid = user[0]
        nickname = user[1]
        # 判断 uid 在 list 中出现的次数
        uid_times[uid] += 1
        if uid_times[uid] == 1:
            is_in_db = get_user_in_db_by_uid(user[0])
            user_result = User(uid, nickname, is_in_db)
        else:
            print(f'>>> 用户{user[1]}在本列表中出现过')
            user_result = User(uid, nickname, True)
        yield user_result


def pre_user_list():
    """返回预先的用户列表"""
    file = get_user_file_name()
    users = extract_user_from_file(file)
    return generate_query_result(users)


def insert_into_maidian(users, owner1):
    """预先把已经在数据库的内容插入埋点"""
    print('当前过滤 ', owner1, ' 的消息')
    db_pool = get_db_tool()
    conn = db_pool.connection()
    cursor = conn.cursor()

    insert_maidian_sql = "INSERT INTO douyin_maidian (suren_id, nickname, is_new, update_time, mark) VALUES (%s, %s, %s, NOW(), %s)"
    try:
        i = 0
        for item in users:
            i += 1
            print(i, '做参考：', item)
            if item.in_db:
                print('用户【', item.nickname, '】入库')
                # for i in range(10):
                result = cursor.execute(insert_maidian_sql, (item.uid, item.nickname, False, owner1))
                conn.commit()
    except:
        traceback.print_exc()
        conn.rollback()
    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    file = get_user_file_name()
    users = extract_user_from_file(file)
    result = generate_query_result(users)
    insert_into_maidian(result, '')
    print('清空数据')
    clean_dir('d:\\douyin')
    clean_dir("d:\\douyin2")
