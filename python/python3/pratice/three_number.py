# -*- coding: utf-8 -*-
"""
file: three_number.py
"""
import sys
import os


os.chdir('/home/nhb/workspace/github/Script/python/python3/pratice')


class MyNumbers(object):
    def __init__(self):
        self.b = 3

    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a < 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
    
    def test(self):
        print('MyNumbers')


class ReMyNumbers(MyNumbers):
    def test(self):
        print('ReMyNumbers')


xy = ReMyNumbers()
print(xy.test())


class Private(object):
    __secret_count = 0
    public_count = 0

    def count(self):
        self.__secret_count += 1
        self.public_count += 1
        print(self.__secret_count)


count = Private()
count.count()
print(count.public_count)
print(count.__secret_count)
