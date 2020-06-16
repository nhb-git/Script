# -*- coding: utf-8 -*-
# class A:
#     __x = 3
#     def __init__(self, name):
#         self.__name = name
#
#     def __foo(self):
#         print('run foo')
#
#     def bar(self):
#         self.__foo()
#         print('bar')
#
#
# print(A.__dict__)
# # print(A.__x)
# a = A('niu')
# a.bar()
"""
    1. 在类外部无法直接访问到__x 这样以双下划线开头的属性
    2. 子类无法覆盖父类以__开头的属性
"""


class A:
    def __foo(self):
        print('A foo')

    def bar(self):
        print('A bar')
        self.__foo()


class B(A):
    def __foo(self):
        print('B foo')


b = B()
b.bar()
