# -*- coding: utf-8 -*-
import functools


def log(func):
    @functools.wraps(func)
    def wrapper(a, b):
        print('start execute')
        func()
        print('end execute')
    return wrapper


@log
def my_func(a, b):
    print('a+b=%d'.format(a+b))


# my_func = log(my_func)
my_func()
print(my_func.__name__)
