# -*- coding: utf-8 -*-
from multiprocessing import Process


class MyProcess(Process):
    def __init__(self, name):
        super(MyProcess, self).__init__()
        self.name = name

    def run(self):
        print('测试%s多进程' % self.name)
