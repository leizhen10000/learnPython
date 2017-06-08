#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'leizhen'
__mtime__ = '2017/6/27'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
import os


class FormatCode(object):
    def __init__(self):
        pass

    @staticmethod
    def format_card_info(info):
        key_list = info.keys()
        result_list = []
        for key in key_list:
            result_list.append('Assert.assertEquals(orderInfo.get("' + key + '").toString(), "百度渠道");\n')
            # Assert.assertEquals(orderInfo.get("serialId").toString(), "百度渠道");
        file_path = os.path.join(os.getcwd(), "format.txt")
        with open(file_path, "w") as f:
            f.writelines(result_list)


if __name__ == '__main__':
    info = {
        "serialId": "百度渠道",
        "orderId": 162294,
        "riderTel": "",
        "customerTel": "13204020965",
        "address": "浙江省杭州市下城区东新街道善贤路中国杭州国际人力资源产业园详细地址",
        "extraFee": 100,
        "distance": "0.3km",
        "sinceOrdered": 11,
        "isAddExtraFee": True,
        "orderStatusCn": "派单中",
        "orderStatus": 0,
        "platformDesc": "百度外卖",
        "extraFeeDisplay": "1元",
        "superiorShowed": False,
        "riderId": ""
    }
    FormatCode().format_card_info(info=info)
