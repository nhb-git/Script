# -*- coding: utf-8 -*-

"""
递归函数练习
"""


def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)


print(fact(5))
