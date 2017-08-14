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
            value = info.get(key)

            # 把所有的key转化成，dto.get形式
            # if not isinstance(value, list):
            #     result_list.append('Assert.assertEquals(respBalanceDetail.get("' + key + '"), balanceDetail.get' +
            #                        str(key)[:1].upper() + str(key)[1:] + '());\n')

            # 把所有的key转换成，dto.set()的形式
            # if not isinstance(value, list):
            #     result_list.append("orderDTO.set" + str(key)[:1].upper() + str(key)[1:] + "(\"" + str(value) + "\");\n")
            # elif isinstance(value, str):
            #     result_list.append("cardDTO.set" + str(key)[:1].upper() + str(key)[1:] + "(\"" + value + "\");\n")

            # 提取所有key，做成属性
            result_list.append("private String " + key + ";\n")

            # 获取所有的key
            # result_list.append("String " + key + ", ");

            # Map 形式的get set
            # result_list.append(" balanceDetail.set" + str(key)[:1].upper() + str(key)[1:] + "(\" \");\n")

        file_path = os.path.join(os.getcwd(), "format.txt")
        with open(file_path, "w") as f:
            f.writelines(result_list)


if __name__ == '__main__':
    info = {
        "monthlyIncome": 0.0,
        "incomeDetail": {
            "distributionFee": 0.0,
            "reward": 0.0,
            "other": 0.0
        },
        "monthlyExpense": 11.0,
        "expenseDetail": {
            "riskBlockedFund": 10.0,
            "insurancefee": 1.0,
            "successWithdrawal": 0.0,
            "equipmentDeposit": 0.0,
            "other": 0.0
        },
        "balance": 903.1,
        "frozenProvision": 0.0,
        "blockedFund": 0.0,
        "blockedFundDetail": {
            "blockedGoodfee": 0.0,
            "blockedRiskfee": -8.0
        },
        "uncheckedBalance": 621.8,
        "uncheckedBalanceDetail": {
            "distributionFee": 597.7,
            "reward": 10.0,
            "other": 14.1
        },
        "accountCheckingVisible": 0
    }
    FormatCode().format_card_info(info=info)
