#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
# @Time    : 19/11/19 10:23
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @Site    : http://www.leizhen.com
# @File    : parser.py
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
import _io
import io
import os
import warnings
from collections import OrderedDict
from contextlib import contextmanager
from typing import Union, Text, IO, Iterator, Dict, Optional, Tuple, NamedTuple, Pattern, Sequence

KeyValuePair = NamedTuple("KeyValuePair", [("key", Optional[Text]),
                                           ("value", Optional[Text]),
                                           ("original", Text)])

_whitespace = None  # todo: 需要添加正则表达式


class LouEnv():

    def __init__(self, env_path, verbose=False, encoding=None):
        # type: (Union[Text,os.PathLike,_io.StringIO],bool,Union[None, Text]) -> None
        self.env_path = env_path  # type: Union[Text, os.PathLike, _io.StringIO]
        self.verbose = verbose  # type: bool
        self.encoding = encoding  # type: Union[None,Text]
        self._dict = None  # type: Optional[Dict[Text,Text]]

    @contextmanager
    def _get_stream(self):
        # type: () -> Iterator[IO[Text]]
        if os.path.isfile(self.env_path):
            with io.open(self.env_path, encoding=self.encoding) as stream:
                yield stream
        else:
            if self.verbose:
                warnings.warn(F"文件不存在 {self.env_path}")  # type: ignore
            yield _io.StringIO('')

    def get_env_dict(self):
        # type: () -> Dict[Text,Text]
        """以字典形式返回变量"""
        if self._dict:
            return self._dict

        values = OrderedDict(self.parse())
        self._dict = resolve_nested_variables(values)
        return self._dict

    def parse(self):
        # type: () -> Iterator[Tuple[Text,Text]]
        with self._get_stream() as stream:
            for mapping in None:
                pass
            # todo: 添加对文件的读取


def resolve_nested_variables(values):
    pass


def parse_binding(reader):
    # type: (Reader) -> KeyValuePair
    reader.set_mark()  # mark 有什么用
    try:
        reader.read_regex(_whitespace)
        # todo: 其他的正则
    except Exception:
        pass


class Reader:
    def __init__(self, stream):
        # type: (IO[Text]) -> None
        self.string = stream.read()
        self.position = 0
        self.mark = 0

    def has_next(self):
        # type: () -> bool
        return self.position < len(self.string)

    def set_mark(self):
        # type: () ->None
        self.mark = self.position

    def get_mark(self):
        # type: ()->Text
        return self.string[self.mark:self.position]

    def read_regex(self, regex):
        # type: (Pattern[Text]) -> Sequence[Text]
        match = regex.match(self.string, self.position)
        if match is None:
            raise Exception("正则匹配没有结果")
        self.position = match.end()
        return match.groups()


def parse_stream(stream):
    # type: (IO[Text]) -> Iterator[KeyValuePair]
    reader = Reader(stream)
    while reader.has_next():
        try:
            yield
        except:
            pass
