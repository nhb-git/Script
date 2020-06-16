# -*- coding: utf-8 -*-
class People:
    def __init__(self, name, weight, height):
        self.name = name
        self.weight = weight
        self.height = height

    @property
    def bmi(self):
        # self.__bmi = self.weight / (self.height ** 2)
        return self.__bmi

    @bmi.setter
    def bmi(self, val):
        self.__bmi = val

    @bmi.deleter
    def bmi(self):
        print('deleter')


p = People('Davis', 70, 1.73)
p.bmi = 3
print(p.bmi)
