# -*- coding: utf-8 -*-
"""
@filename: test_class.py
@author: haibao
"""


class People():
    name = ""
    age = 0
    __weight = 0

    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print('%s say: he is %d' % (self.name, self.age))


class Student(People):
    grade = 0

    def __init__(self, n, a, w, g):
        People.__init__(self, n, a, w)
        self.grade = g

    def speak(self):
        print(
            '%s say: he is %d, grade is %d' % (self.name, self.age, self.grade)
        )


class Speaker():
    def __init__(self, n, t):
        self.name = n
        self.topic = t

    def speak(self):
        print("%s is a speaker, he's topic is %s" % (self.name, self.topic))


class Sample(Speaker, Student):
    def __init__(self, n, a, w, g, t):
        Student.__init__(self, n, a, w, g)
        Speaker.__init__(self, n, t)
        self.__private = 3

    def speak(self):
        print(self.__private)


class Vector():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(str(v1 + v2))
