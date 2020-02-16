# -*- coding: utf-8 -*-
"""
面向对象：属性和动作的结合体
优点:
    1. 可扩展性强
缺点: 编程复杂度提高
应用场景：适用于用户需求经常改变的场景

类: 某一角度一系列对象共同特点和动作的抽象

在实际场景中，有具体的某个对象，总结这个对象的特点和动作技能
    对象1:
        特点:
            名字：甲
            年龄：18
            学校: 甲
        动作技能:
            吃饭
            喝水
            睡觉
    对象2:
        特点：
            名字：乙
            年龄：19
            学校：2
        动作技能：
            吃饭
            学习
            喝水
            睡觉
"""


# 定义类
class Student:
    school = 'luffi'

    def learn(self):
        print('is learning')

    def eat(self):
        print('is eating')

    def sleep(self):
        print('is sleep')


# 创建对象
stu1 = Student()
stu2 = Student()
stu3 = Student()
print(stu1)
print(stu2)
print(stu3)

