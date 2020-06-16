# -*- coding: utf-8 -*-
# class Foo:
#     def __init__(self, name):
#         self.name = name
#
#     def tell(self):
#         return self.name
#
#     @classmethod
#     def func(cls):
#         print(cls)
#
#     @staticmethod
#     def func1(x, y):
#         print(x, y)
#         return
#
#
# Foo.func1(3, 4)
# f = Foo('niu')
# f.func1(4, 5)
import hashlib
import time
from common_models import setting


class People:
    def __init__(self, name, age, sex):
        self.id = self.create_id()
        self.name = name
        self.age = age
        self.sex = sex

    def tell_info(self):
        print('name: %s, age: %s, sex: %s' % (self.name, self.age, self.sex))

    @classmethod
    def from_conf(cls):
        obj = cls(
            setting.name,
            setting.age,
            setting.sex
        )
        return obj

    @staticmethod
    def create_id():
        m = hashlib.md5(str(time.time()).encode('utf-8'))
        return m.hexdigest()


# 绑定方法：对象方法, 自动将对象本身作为第一个参数传入
# p = People('niu', 18, 'man')
# p.tell_info()

# 绑定方法：类方法, 自动将类本身作为第一个参数传入
# p = People.from_conf()
# p.tell_info()

# 非绑定方法: 不需要传入固定参数，谁都可以调用
p1 = People('niu', 18, 'man')
p2 = People('niu1', 28, 'man')
p3 = People('niu2', 38, 'man')
print(p1.id)
print(p2.id)
print(p3.id)
