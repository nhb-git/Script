# -*- coding: utf-8 -*-
class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        pass


# obj = People('niu', 20)
# 反射：通过字符串映射到对象的属性
# print(hasattr(obj, 'name'))  # obj.__dict__['name']
# print(hasattr(obj, 'talk'))  # obj.__dict__['talk']
# print(getattr(obj, 'name'))
# print(getattr(obj, 'name1', None))
# setattr(obj, 'name', 'hai')
# print(obj.name)
# setattr(obj, 'name', 'bao')
# print(obj.name)

# 反射的应用
class Service:
    def run(self):
        while True:
            cmd = input(':>>').strip()
            if hasattr(self, cmd):
                func = getattr(self, cmd)
                func()

    def get(self):
        print('get....')

    def put(self):
        print('put....')


s = Service()
s.run()
