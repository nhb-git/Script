# 定义类
class Student:
    school = 'luffi'    # 数据属性

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def learn(self):    # 函数属性
        print('{0} is learning'.format(self.name))

    def eat(self):
        print('is eating')

    def sleep(self):
        print('is sleep')


stu1 = Student('niu', 16, 'male')
stu2 = Student('hai', 26, 'male')


# 类中的数据属性： 是所有对象共有的
print(Student.school)
print(stu1.school)

# 类中的函数属性： 绑定到对象的, 绑定到不同对象是不同的绑定方法
# print(Student.learn)
# print(stu1.learn)
# print(stu2.learn)
# Student.learn(stu1)
# Student.learn(stu2)
# stu1.learn()
# stu2.learn()
Student.x = 'XX'
print(stu1.__dict__)
print(stu1.x)
