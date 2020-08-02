#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：8/2/2020  9:59 PM 
# 文件名称   ：1 开启线程的两种方式.py
import time
from threading import Thread


def piao(name):
    print('%s piaoing' % name)
    import random
    time.sleep(random.randrange(1, 5))
    print('%s piaoning end' % name)


if __name__ == '__main__':
    t1 = Thread(target=piao, args=('egon',))
    t1.start()
    print('主')
