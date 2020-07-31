#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：7/30/2020  10:56 PM 
# 文件名称   ：4 守护进程.py
import time
from multiprocessing import Process


def task(name):
    print('%s is running' % name)
    time.sleep(2)


if __name__ == '__main__':
    p = Process(target=task, args=('子进程1',))
    p.daemon = True     # 设置为守护进程，必须在start之前运行
    p.start()
    print('主')
