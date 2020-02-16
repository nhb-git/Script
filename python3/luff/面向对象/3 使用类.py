# -*- coding: utf-8 -*-


# 定义类
class Student:
    school = 'luffi'    # 数据属性

    def learn(self):    # 函数属性
        print('is learning')

    def eat(self):
        print('is eating')

    def sleep(self):
        print('is sleep')


Student.contry = 'CN'
print(Student.__dict__)
print(Student.contry)

del Student.contry
Student.school = '甲'
print(Student.__dict__)

