name = 'niu'

# global用来声明全局变量
# 在函数外部创建的变量为全局变量，在函数内部创建的变量为局部变量
# 使用变量时，先局部变量再全局变量
# locals() 打印本地的变量信息
# globals() 打印全局的变量信息


def print_name():
    global name
    name = 'hai'
    age = 26
    print(name)
    print(locals())
    print(globals())


print_name()
print(name)
