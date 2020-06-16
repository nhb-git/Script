# -*- coding: utf-8 -*-


def fib(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a+b
        yield a


for i in fib(100):
    print(i)
