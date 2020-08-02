#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：8/2/2020  10:26 PM 
# 文件名称   ：2 Thread对象的其他属性和方法.py
import time
from threading import Thread, currentThread, active_count, enumerate


def task():
    print('%s is running' % currentThread().getName())
    print('%s is end' % currentThread().getName())


if __name__ == '__main__':
    t = Thread(target=task, name='thread-123')
    t.setName('thread-12')
    print(t.getName())
    t.start()
    t.join()
    print(t.is_alive())
    # print(active_count())
    # print(enumerate())
