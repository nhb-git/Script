# -*- coding: utf-8 -*-


def outer():
    name = 'niu'

    def inner():
        print('inner', name)
    return inner


func = outer()
print(func())
