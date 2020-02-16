# __init__ 方法是为对象定义自己独有的特征
# 定义类
class Student:
    school = 'luffi'    # 数据属性

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def learn(self):    # 函数属性
        print('is learning')

    def eat(self):
        print('is eating')

    def sleep(self):
        print('is sleep')


stu1 = Student('niu', 16, 'male')

# 实例化的步骤
# 1. 产生一个空对象stu1
# 2. Student.__init__(stu1, 'niu', 16, 'mail')
print(stu1.__dict__)

