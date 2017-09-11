#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'leizhen'
__mtime__ = '2017/8/10'
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

import re


class FormatCode(object):
    def __init__(self, info):
        self._info = info

    def format_code(self):
        result_list = []
        url = self._info.get('url', 'NoName')
        class_name = split_url_2_class_name(url=url)
        if class_name is None:
            class_name = '${NoName}'
        method_name = class_name[0:1].lower() + class_name[1:]
        print class_name
        result_list.append('public class %s {\n' % class_name)
        result_list.append('\n\t// 读取配置文件\n')
        result_list.append('\tprivate Attribute attribute = SystemConstants.getAttribute();\n')
        result_list.append('\n\t@DataProvider(name = "%sData")' % class_name)
        result_list.append(
            '\n\tpublic Iterator<Object[]> dataFortestMethod(Method method) throws IOException {\n'
            '\t\treturn new ExcelDataProvider("/${pathName}/%sData");\n'
            '\t}\n' % class_name)
        result_list.append('\n\t@Test(dataProvider = "%sData")\n' % class_name)
        result_list.append('\tpublic void test%s(Map<String, String> data) throws IOException {\n' % class_name)
        result_list.append('\t\t//dosomething\n'
                           '\t}\n')
        param_list = key_list(info['params'])
        param_string = ''
        for param in param_list:
            param_string += 'String %s, ' % param
        result_list.append('\n\tpublic void %sRequest(%s String token){\n' % (method_name, param_string))
        result_list.append(
            '\t\tRestAssured.baseURI="http://" + attribute.getRiderHost() + ":" + attribute.getRiderPort();\n')
        result_list.append('\t\tString url="/" + attribute.getRiderVersion() + "%s";\n' % url)
        result_list.append('\t\tMap<String,String> param = new HashMap<String, String>();\n')
        for param in param_list:
            result_list.append('\t\tparam.put("%s",%s);\n' % (param, param))
        result_list.append('\t\tparam.put("token",token);\n')
        result_list.append('\t\tString sign= SignUtils.getSign(param);\n')
        result_list.append('\t\tparam.put("sign",sign);\n')
        result_list.append('\n\t\tResponse response=given().params(param).when().%s(url)\n' % info.get('method', 'get'))
        result_list.append('\t\tlogger.info(">>>>> %s params       ：" + param);\n' % class_name)
        result_list.append('\t\tlogger.info(">>>>> %s response    ：" + response.asString());\n' % class_name)
        result_list.append('\t\treturn response;\n\t}\n')
        # response check
        result_list.append('\t\t//验证response\n')
        result_list.append(
            '\n\tpublic void check%sSuccess(Response %sResponse,Map<String,String> data}) {\n'
            % (class_name, method_name))
        result_list.append('\t\t%sResponse.\n'
                           '\t\t\tthen().\n'
                           '\t\t\tassertThat().statusCode(200).\n'
                           '\t\t\tbody("status",equalTo("${something}"));\n\t}\n' % method_name)

        file_path = os.path.join(os.getcwd(), "format.txt")

        with open(file_path, "w") as f:
            f.writelines(result_list)

        print result_list


def key_list(param_info):
    result_list = []
    split_list = map(lambda m: re.split(r'_', m), param_info)  # 去除参数中的下划线 order_stand --> order stand
    for item in split_list:
        temp_item = reduce(lambda m, n: m[0:1].upper() + m[1:] + n[0:1].upper() + n[1:], item)  # 拼接成title格式
        result_list.append(temp_item[0:1].lower() + temp_item[1:])  # 将转换好的结果传入
    return result_list

    # 获取所有的key
    # result_list.append("String " + key + ", ");


def split_url_2_class_name(url):
    # test = '/rider/obtain-good.json'
    result = re.split(r'[/.]', url)[-2]
    method_list = re.split(r'-', result)
    name = ''
    for item in method_list:
        name += item.title()
    return name


if __name__ == '__main__':
    info = {
        "url": "/rider/obtain-good.json",
        "method": 'get',
        "params": [
            "order_standard_category",
            "monthlyExpense",
            "balance",
            "frozenProvision",
            "blockedFund",
        ],
        "result": {
            "code": "0000",
            "msg": "success"
        }

    }
    FormatCode(info=info).format_code()
    # key_list(info)
