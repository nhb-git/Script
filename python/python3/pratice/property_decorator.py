# -*- coding: utf-8 -*-
import functools


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('start execute')
        func(*args, **kw)
        print('end execute')
    return wrapper


@log
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
s.age = 20
print(s.birth)
print(s.age)
