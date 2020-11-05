#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2020/11/5 11:29
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @File    : gen_universe_file.py
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
# 生成 java 自动化用例代码

import requests

host = 'http://40.73.96.103/universe'


def login():
    url = 'http://40.73.96.103/universe/login'
    params = {
        "userName": "testadmin",
        "userPassword": 123456
    }
    headers = {'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2'}
    resp = session.post(url, params, headers=headers)
    print(resp.text)


def get_api_doc():
    url = host + '/v2/api-docs'
    return session.get(url).json()


def filter_tag(all_path, tag_name):
    for path, detail in all_path.items():
        for req_type, remains in detail.items():
            print(req_type)
            print(remains)
            if tag_name in remains.get('tags'):
                print(path)
                print(type)
                print()


if __name__ == '__main__':
    session = requests.Session()
    login()
    resp_json = get_api_doc()
    paths = resp_json.get('paths')
    filter_tag(paths, "DATA_CENTER_TAG")
