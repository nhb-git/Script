#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：7/30/2020  8:20 PM 
# 文件名称   ：2 查看进程pid.py
import os
import time
from multiprocessing import Process


def task():
    print('%s is running' % os.getpid())
    time.sleep(3)
    print('%s is done' % os.getpid())
    print(os.getppid())


if __name__ == '__main__':
    p = Process(target=task)
    p.start()
    print(os.getpid())
    print(os.getppid())
