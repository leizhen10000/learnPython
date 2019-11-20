#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
# @Time    : 19/11/11 13:27
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @Site    : http://www.leizhen.com
# @File    : extract_promotion_detail.py
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
import json
import os
import re
from datetime import datetime
from pprint import pprint

from openpyxl import Workbook


def create_excel(file_path):
    wb = Workbook(write_only=True)
    wb.create_sheet('素人账号信息')
    wb.create_sheet('商品橱窗信息')
    wb.create_sheet('账号运营信息')
    wb.save(file_path)


def format_promotion(json_data):
    result = json.loads(json_data)
    promotions = result.get('promotions')
    for promotion in promotions:
        sales = promotion.get('sales')
        title = promotion['title']
        visitor_count = '{:,d}'.format(promotion['visitor']['count'])
        price = promotion.get('price', 0) / 100.0
        last_aweme_id = promotion.get('last_aweme_id')  # 对应视频id
        promotion_id = promotion['promotion_id']
        goods_source = promotion['goods_source']
        coupon_url, coupon_real_price = None, None
        coupon = promotion.get('apply_coupon_button')
        if coupon:
            coupon_url = coupon.get('h5_url')
            coupon_real_price = re.findall(r'\d+\.*\d*', coupon.get('text')[0])[0]
        elastic_title = promotion.get('elastic_title')
        elastic_type = promotion.get('elastic_type')
        detail_url = promotion.get('detail_url')
        # line = f'名称：{title}，\n\t销量：{sales}，访客：{visitor_count}，价格：{price}'
        # print(line)
        promotion_dict = {'名称': title, '销量': sales, '访客': visitor_count, '价格': price, '商品id': promotion_id,
                          '商品来源': goods_source, '优惠后价格': coupon_real_price, '弹性标题': elastic_title, '弹性类型': elastic_type,
                          '关联视频id': last_aweme_id, '优惠券链接': coupon_url, '商品详情链接': detail_url}
        yield promotion_dict


def format_user_info(json_data):
    result = json.loads(json_data)
    user = result['user']
    uid = user.get('uid')
    total_favorited = user.get('total_favorited')  # 获赞量
    following_count = user.get('following_count')  # 关注量
    follower_count = user.get('follower_count')  # 粉丝量
    aweme_count = user.get('aweme_count')  # 作品数
    dongtai_count = user.get('dongtai_count')  # 动态数
    favoriting_count = user.get('favoriting_count')  # 喜欢量
    bind_phone = user.get('bind_phone')  # 绑定手机
    bind_phone = bind_phone if bind_phone != '#' else ''
    signature = user.get('signature')  # 签名，可能包含手机号和微信号
    nickname = user.get('nickname')  # 昵称
    with_fusion_shop_entry = user.get('with_fusion_shop_entry')  # 是否有商品橱窗
    user_url = user['share_info']['share_url']  # 用户详情链接
    user_qr_code_url = user['share_info']['share_qrcode_url']['url_list']
    if len(user_qr_code_url) > 0:
        user_qr_code_url = user_qr_code_url[0]

    user_dict = {'素人id': uid, '获赞量': total_favorited, '关注量': following_count, '作品数': aweme_count,
                 '动态数': dongtai_count, '粉丝量': follower_count, '喜欢量': favoriting_count, '绑定手机': bind_phone,
                 '签名': signature, '昵称': nickname, '是否有商品橱窗': with_fusion_shop_entry, '用户详情链接': user_url,
                 '用户详情二维码链接': user_qr_code_url}
    yield user_dict


def form_aweme(json_data):
    data = json.loads(json_data)
    aweme_list = data['aweme_list']
    for aweme in aweme_list:
        # 作品详情
        statistic = aweme['statistics']
        digg_count = statistic['digg_count']  # 点赞量
        comment_count = statistic['comment_count']  # 评论量
        share_count = statistic['share_count']  # 分享量
        download_count = statistic['download_count']  # 下载量
        forward_count = statistic['forward_count']  # 转发量
        aweme_id = aweme['aweme_id']  # 作品id
        author_user_id = str(aweme['author_user_id'])  # 用户id
        # 分类
        text_extra = aweme['text_extra']
        tag = []
        for text in text_extra:
            if 'hashtag_name' in text:
                tag.append(text['hashtag_name'])
        tag = ','.join(tag)  # 标签
        desc = aweme['desc']  # 视频标题
        create_time = datetime.fromtimestamp(int(aweme['create_time']))  # 创建时间
        yield {'视频id': aweme_id, '素人id': author_user_id, '点赞量': digg_count, '评论量': comment_count,
               '分享量': share_count, '下载量': download_count, '转发量': forward_count, '标签': tag,
               '视频标题': desc, '创建时间': create_time}


import pandas as pd

base_dir = 'D:\\douyin'
all_files = os.listdir('D:\\douyin')

# 获取配置文件
env_file = os.path.abspath(os.path.join(os.path.relpath(__file__), os.path.pardir, '.env'))

for file in all_files:
    file_dir = os.path.join(base_dir, file)
    file_name = os.path.splitext(file)[0]

    if 'promotion' in file_name:
        with open(file_dir, 'rt', encoding='gbk') as f:
            line = f.readline()
            # 写入 excel
            df = pd.DataFrame(list(format_promotion(line)))
            user_id = re.match(r'(\d+)', file_name).groups()[0]
            writer = pd.ExcelWriter(f'{user_id}_promotion.xlsx')
            df.to_excel(writer, sheet_name='商品橱窗')
            writer.close()
        # todo: 先这样处理，后期放在数据库中
        # 写入 数据库
        # todo
    elif 'user' in file_name:
        with open(file_dir, 'rt', encoding='utf-8') as f:
            line = f.readline()
            df = pd.DataFrame(list(format_user_info(line)))
            user_id = df['素人id'].values[0]
            # if not os.path.exists(f'{user_id}.xls'):
            writer = pd.ExcelWriter(f'{user_id}_user.xlsx')
            df.to_excel(writer, sheet_name='素人信息')
            writer.close()
    elif 'zuopin' in file_name:
        with open(file_dir, 'rt', encoding='utf-8') as f:
            line = f.readline()
            df = pd.DataFrame(list(form_aweme(line)))
            user_id = df['素人id'].values[0]
            df.to_excel(f'{user_id}_zuopin.xlsx', sheet_name='作品信息')
