# -*- coding: utf-8 -*-
def unzip_package(*number):
    for i in number:
        print(i)


def unzip_dict_package(**kw):
    print(kw)


def person(name, age, *, city, job):
    print(name, age, city, job)


L = [1, 3, 4]
D = {'m': 1, 'n': 5}
unzip_package()
unzip_dict_package(x=1, y=3)
unzip_dict_package(**D)
person('niu', 26, city='beijing', job='it')
