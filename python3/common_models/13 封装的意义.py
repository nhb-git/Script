# -*- coding: utf-8 -*-
class People:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_info(self):
        print('name is <%s>, age is <%s>' % (self.__name, self.__age))

    def set_info(self, name, age):
        if not isinstance(name, str):
            print('name not str')
            return
        if not isinstance(age, int):
            print('age not int')
            return
        self.__name = name
        self.__age = age


p = People('niu', 28)
p.get_info()
p.set_info('hai', 29)
p.get_info()
p.set_info(3, 29)
p.get_info()

"""
    1. 封装数据：控制外部用户修改数据的方式
    2. 封装方法：隔离复杂度
"""
