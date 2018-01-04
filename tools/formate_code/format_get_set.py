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
        self._result_list = []
        self._class_name = ''
        self._method_name = ''
        self._param_list = key_list(info['params'])

    def format_code(self):
        url = self._info.get('url', 'NoName')
        self._class_name = split_url_2_class_name(url=url)
        if self._class_name is None:
            self._class_name = '${NoName}'
        self._method_name = self._class_name[0:1].lower() + self._class_name[1:]

        # 定义 class 格式
        self._result_list.append('public class %s {\n' % self._class_name)
        self._result_list.append('\n\t// 读取配置文件\n')
        self._result_list.append('\tprivate Attribute attribute = SystemConstants.getAttribute();\n')
        # 定义 data provider 方法
        self._result_list.append('\n\t@DataProvider(name = "%sData")' % self._class_name)
        self._result_list.append(
            '\n\tpublic Iterator<Object[]> dataFortestMethod(Method method) throws IOException {\n'
            '\t\treturn new ExcelDataProvider("/${pathName}/%sDataProvider");\n'
            '\t}\n' % self._class_name)
        self._result_list.append(
            '\n\t@Test(dataProviderClass = ${dataProviderClassName},dataProvider = "%sData")\n' % self._class_name)
        self._result_list.append(
            '\tpublic void test%s(Map<String, String> data) throws IOException {\n' % self._class_name)
        self._result_list.append('\t\t//doSomething\n'
                                 '\t}\n')
        # 定义 发起请求的方法
        self.request_method(has_token=True)
        self._result_list.append(
            '\t\tRestAssured.baseURI="http://" + attribute.getRiderHost() + ":" + attribute.getRiderPort();\n')
        self._result_list.append('\t\tString url="/" + attribute.getRiderVersion() + "%s";\n' % url)
        self._result_list.append('\t\tMap<String,String> param = new HashMap<String, String>();\n')
        for param in self._param_list:
            self._result_list.append('\t\tparam.put("%s",%s);\n' % (param, param))
        self._result_list.append('\t\tparam.put("token",token);\n')
        self._result_list.append('\t\tString sign= SignUtils.getSign(param);\n')
        self._result_list.append('\t\tparam.put("sign",sign);\n')
        self._result_list.append(
            '\n\t\tResponse response=given().params(param).when().%s(url)\n' % info.get('method', 'get'))
        self._result_list.append('\t\tlogger.info(">>>>> %s params       ：" + param);\n' % self._class_name)
        self._result_list.append(
            '\t\tlogger.info(">>>>> %s response    ：" + response.asString());\n' % self._class_name)
        self._result_list.append('\t\treturn response;\n\t}\n')

        # response check
        self._result_list.append('\n\t//验证response')
        self._result_list.append(
            '\n\tpublic void check%sSuccess(Response %sResponse,Map<String,String> data}) {\n'
            % (self._class_name, self._method_name))
        self._result_list.append('\t\t%sResponse.\n'
                                 '\t\t\tthen().\n'
                                 '\t\t\tassertThat().statusCode(200).\n'
                                 '\t\t\tbody("status",equalTo("${something}"));\n\t}\n' % self._method_name)

        file_path = os.path.join(os.getcwd(), "format.txt")

        with open(file_path, "w") as f:
            f.writelines(self._result_list)

        print self._result_list

    """
    发起请求的方法，包含所有参数
    has_token 表示是否包含 token 参数，跟 app/crm 相关的都有token，token = False
    """

    def request_method(self, has_token=False):
        param_string = ''
        for param in self._param_list:
            param_string += 'String %s, ' % param
        if has_token:
            self._result_list.append('\n\tpublic void %sRequest(%s){\n' % (self._method_name, param_string[:-2]))
        else:
            self._result_list.append(
                '\n\tpublic void %sRequest(%s String token){\n' % (self._method_name, param_string))


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
        "url": "/api/eleme/order/get-order.json",
        "method": 'post',
        "params": [
            "order_original_id"
        ],
        "result": {
            "code": "0000",
            "msg": "success"
        }

    }
    FormatCode(info=info).format_code()
    # key_list(info)
