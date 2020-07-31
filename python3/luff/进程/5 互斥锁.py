#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：7/30/2020  11:09 PM 
# 文件名称   ：5 互斥锁.py
import time
from multiprocessing import Process, Lock


def task(name, metux):
    metux.acquire()
    print('%s 1' % name)
    time.sleep(1)
    print('%s 2' % name)
    time.sleep(1)
    print('%s 3' % name)
    metux.release()


if __name__ == '__main__':
    metux = Lock()
    for i in range(3):
        p = Process(target=task, args=('进程%s' % i, metux))
        p.start()
