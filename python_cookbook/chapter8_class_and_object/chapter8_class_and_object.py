#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2019/11/9 08:36
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @File    : chapter8_class_and_object.py
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
from datetime import date

x: int = 1
a = eval('x+1')
a = a + 1
print(a)

exec('print(x+1)')

expr = """print(x, y)"""
exec(expr, {'x': 1, 'y': 2}, {'y': 'two'})
print('globals 中的值会被 locals 中的值覆盖')


class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Pair({self.x}, {self.y})'

    def __str__(self):
        return f'({self.x}, {self.y})'


p = Pair(2, 3)
print(repr(p))
print(p)

print('\n')
print('处理日期')
print('format() 在类中对应实现了 __format__() 方法')
d = date(2019, 10, 10)
print(format(d))
print(format(d, '%A %B %d %Y'))

print('\n')
print('让对象支持上下文管理协议（with语句）')
print('调用上下文管理器中的__enter__方法，在其中执行一些预处理工作')
print('__enter__ 返回值赋值给 as 声明的变量')
print('再执行with语句中的代码块，声明的变量可以作为通用变量使用')
print('最后调用 __exit__ 方法')
print('三个参数： exc_type, exc_val, exc_tb，异常类型、异常值、回溯信息')
print('__exit__ 方法返回的值为True，异常被忽视')
print('实现打开文件操作')


class MyOpen:

    def __init__(self, file_name):
        """初始化"""
        self.file_name = file_name
        self.file_handler = None
        return

    def __enter__(self):
        """返回 file_handler """
        print('enter: ', self.file_name)
        self.file_handler = open(self.file_name, 'r')
        return self.file_handler

    def __exit__(self, exc_type, exc_val, exc_tb):
        """关闭文件并返回 True"""
        print('exit: ', exc_type, exc_val, exc_tb)
        if self.file_handler:
            self.file_handler.close()
        return True


with MyOpen('test.txt') as file_in:
    for line in file_in:
        print(line)
        raise ZeroDivisionError

print('python 提供内置的 contextlib 库，使得上下文管理器更加容易使用')

print('\n'
      '在创建大量对象时节省内存方法'
      '创建大量（上百万）的对象，导致占用很大的内存')


class Date:
    __slots__ = ('year', 'month', 'day')

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return f'year: {self.year}, month: {self.month}, day: {self.day}'


d = Date(2019, 10, 15)
d.year = 2018
print(d)
print('__slots__ 的一个常见误区：它昆虫作为一个封装工具来防止用户给实例添加新的属性，'
      '尽管能达到这样的目的，但这不是它的初衷。\n'
      '__slots__ 用来作为一个内存优化工具')

print('\n'
      '双下划线开头的，会导致访问名称变成其他形式')


class B:
    def __init__(self):
        self.__private_method()
        self._internal_method()
        print(self.__private_method)

    def __private_method(self):
        print('this is b class')

    def _internal_method(self):
        print('this is internal method')


class C(B):
    def __init__(self):
        super().__init__()
        self.__private_method()
        self._internal_method()
        print(self.__private_method)

    def __private_method(self):
        print('this is c class')

    def _internal_method(self):
        print('this is c internal method')


c = C()
print('但下划线的内容，会被子类覆盖；\n'
      '而双下划线的内容是一个新内容 B.__private_method  和 C.__private_method ')

print('\n8.7 调用父类方法')
print('在子类中调用父类的某个已经被覆盖的方法')
print('使用 super \n')


class AA():
    def spam(self):
        print('A.spam')


class BB(AA):
    def spam(self):
        print('B spam')
        super().spam()


print('打印 B 和 父类 A 的spam内容')
print(BB().spam())

print(BB.mro())

print('问题：输出的结果为 B.spam A.spam None')
print("查看 mro 路径可以得出结论，mro [<class '__main__.BB'>, <class '__main__.AA'>, <class 'object'>]")
print("python 会从左到右自动获取第一个能匹配该方法 spam 的类，这里第一个类，是原始类 object，它没有spam方法")

print('\t super() 函数两个常见用法：\n'
      '一、用于 __init__() 方法，确保父类中的初始化内容被正确执行\n'
      '二、用于在不同情况下区别使用子类和父类的不同实现方式')


class AAA:
    def __init__(self):
        self.x = 0


class BBB(AAA):
    def __init__(self):
        super(BBB, self).__init__()
        self.y = 1


print('这里会使出 BBB 和 父类 AAA 中定义的两个属性:')
bbb = BBB()
print(f'x: {bbb.x}, y: {bbb.y}')


class Proxy:
    def __init__(self, obj):
        self._obj = obj

    def __getattr__(self, name):
        return getattr(self._obj, name)

    def __setattr__(self, name, value):
        if name.startswith('_'):
            super(Proxy, self).__setattr__(name, value)
        else:
            setattr(self._obj, name, value)


print('如果名称以下划线开头，则使用原始的 setattr() 方法，否则就委派给 _obj 去处理')

print('>> 扩展：')
print('由于super() 可能会调用不是你想用的方法，你应该遵循一些通用原则')
print('一、确保在继承体系中所有 相同名字的方法 都拥有 可兼容的参数签名（比如相同的参数个数和参数名称）')
print('\t这样如果 super() 调用了一个非直接父类方法时不会出错')
print('二、确保所有顶层提供了这个方法的实现')
print('\t这样在 MRO 上查找链肯定可以找到某个确定的方法')
print('\n在定义混入类的时候使用 super() 非常普遍')

print('\n8.8 子类扩展父类中的 property 功能')


class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Except a string')
        self._name = value

    @name.deleter
    def name(self):
        raise AttributeError("Can't delete attribute")


class SubPerson(Person):
    @property
    def name(self):
        print('Getting name')
        return super(SubPerson, self).name

    @name.setter
    def name(self, value):
        print('Setting name to', value)
        super(SubPerson, self).name.__set__(self, value)

    @name.deleter
    def name(self):
        print('Deleting name')
        super(SubPerson, self).name.__delete__()


s = SubPerson('Guido')
print(s.name)
s.name = 'Larry'
print(s.name)
