#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：8/3/2020  11:54 AM 
# 文件名称   ：2 gevent模块.py
import gevent
from gevent import monkey; monkey.patch_all()


def eat(name):
    print('%s eat 1' % name)
    # gevent.sleep(2)
    time.sleep(3)
    print('%s eat 2' % name)


def play(name):
    print('%s play 1' % name)
    # gevent.sleep(1)
    time.sleep(1)
    print('%s play 2' % name)


if __name__ == '__main__':
    import time
    start_time = time.time()
    # 提交任务
    g1 = gevent.spawn(eat, 'niu')
    g2 = gevent.spawn(play, 'hai')

    # g1.join()
    # g2.join()
    gevent.joinall([g1, g2])
    print(time.time() - start_time)
