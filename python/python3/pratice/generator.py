# -*- coding: utf-8 -*-
def fib(max):
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a+b


print(list(fib(10)))
