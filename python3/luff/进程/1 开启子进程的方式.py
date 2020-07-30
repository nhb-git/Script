#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：7/30/2020  8:02 PM 
# 文件名称   ：1 开启子进程的方式.py
import time
from multiprocessing import Process


# 方式1
# def task(name):
#     print('%s is running' % name)
#     time.sleep(3)
#     print('%s is done' % name)
#
#
# if __name__ == '__main__':
#     # Process(target=task, kwargs={'name': '子进程1'})
#     p = Process(target=task, args=('子进程1',))
#     p.start()   # 给操作系统发送信号创建进程
#     print('主')

# 方式2
class MyProcess(Process):
    def __init__(self, name):
        super(MyProcess, self).__init__()
        self.name = name

    def run(self):
        print('%s is running' % self.name)
        time.sleep(3)
        print('%s is done' % self.name)


if __name__ == '__main__':
    p = MyProcess('子进程1')
    p1 = MyProcess('子进程2')
    p.start()
    p1.start()
