# -*- coding: utf-8 -*-
import functools


def log(arg):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print("decorator's args: {0}".format(arg))
            print('start execute')
            func(*args, **kw)
            print('end execute')
        return wrapper
    return decorator


@log('hello world')
def my_func(a, b, c):
    print('a+b+c=%d' % (a+b+c))


# my_func = log(my_func)
my_func(1, 2, 3)
print(my_func.__name__)


class Student(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2014 - self._birth


s = Student()
s.birth = 20
print(s.birth)
print(s.age)
