#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：8/2/2020  11:10 PM 
# 文件名称   ：3 互斥锁.py
import time
from threading import Thread, Lock

n = 100


def task():
    global n
    metux.acquire()
    temp = n
    time.sleep(0.1)
    n = temp - 1
    metux.release()


if __name__ == '__main__':
    metux = Lock()
    res = []
    for i in range(100):
        t = Thread(target=task)
        res.append(t)
        t.start()

    for t in res:
        t.join()
    print('主', n)

