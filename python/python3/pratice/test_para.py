# -*- coding: utf-8 -*-
"""
练习函数参数的使用
"""
__author__ = 'haibao'


def test(a, b, d=1, *args, c=3, **kw):
    print(args, kw, d, c)


test(1, 2, 3, c='hai')
