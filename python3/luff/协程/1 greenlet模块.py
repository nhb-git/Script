#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：8/3/2020  11:40 AM 
# 文件名称   ：1 greenlet模块.py
from greenlet import greenlet


def eat(name):
    print('%s eat 1' % name)
    g2.switch('niu')
    print('%s eat 2' % name)
    g2.switch('niu')


def play(name):
    print('%s play 1' % name)
    g1.switch('niu')
    print('%s play 2' % name)


if __name__ == '__main__':
    g1 = greenlet(eat)
    g2 = greenlet(play)
    g1.switch('niu')
