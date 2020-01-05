# -*- coding: utf-8 -*-
class A(object):
    def __init__(self):
        print('A')


class B(A):
    def __init__(self):
        super(B, self).__init__()
        print('B')


if __name__ == "__main__":
    b = B()
