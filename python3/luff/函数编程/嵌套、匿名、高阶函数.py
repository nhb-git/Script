# -*- coding: utf-8 -*-
# 嵌套函数
## name = '全局niu'


## def change():
    ## # name = 'change niu'
    ## def change2():
        # name = 'change2 niu'
        ## print(name)
    ## change2()
    ## print(name)


## change()
## print(name)


# 匿名函数
def cal(x):
    return x**2


for i in map(lambda x: x**2, [1, 2, 3]):
    print(i)

print(3) if 3 > 2 else print(2)
