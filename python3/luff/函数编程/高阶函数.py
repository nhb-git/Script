# 高阶函数：
#   1. 一个或多个函数作为输入
#   2. 返回另外一个函数


def get_abs(n):
    return int(str(n).strip('-'))


def add(x, y, f):
    return f(x) + f(y)


print(add(1, -9, get_abs))
