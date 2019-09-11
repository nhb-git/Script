# -*- coding: utf-8 -*-
L = [1, 2, 3]
iL = iter(L)
while True:
    try:
        print(next(iL))
    except StopIteration:
        break

def lazy_sum(*args):
    def sum():
        ax = ax +1
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1, 3, 5, 7)
print(f())

def create_counter():
    def counter():
        i = 0
        while