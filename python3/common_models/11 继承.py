# -*- coding: utf-8 -*-
class ParentClass1:
    x = 2


class ParentClass2:
    pass


class SubClass1(ParentClass1):
    pass


class SubClass2(ParentClass1, ParentClass2):
    x = 3


print(ParentClass2.__bases__)
print(SubClass1.x)
print(SubClass2.x)
print(SubClass2.mro())
