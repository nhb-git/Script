#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：7/31/2020  7:51 AM 
# 文件名称   ：6 模拟抢票.py
import time
import json
from multiprocessing import Process, Lock


def search(name):
    time.sleep(1)
    dic = json.load(open('6 db.txt', encoding='utf-8'))
    print('%s 剩余票数为%s' % (name, dic['count']))


def get(name):
    time.sleep(1)
    dic = json.load(open('6 db.txt', encoding='utf-8'))
    if dic['count'] > 0:
        dic['count'] -= 1
        time.sleep(2)
        json.dump(dic, open('6 db.txt', 'w', encoding='utf-8'))
        print('%s 购票成功' % name)


def task(name, metux):
    search(name)
    metux.acquire()
    get(name)
    metux.release()


if __name__ == '__main__':
    metux = Lock()
    for i in range(10):
        p = Process(target=task, args=('进程%s' % i, metux))
        p.start()
