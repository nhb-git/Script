#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：8/2/2020  3:48 PM 
# 文件名称   ：7 队列的使用.py
from multiprocessing import Queue


# 创建队列对象并设置队列的最大消息数量为3
q = Queue(3)
q.put('hello')
q.put({'a': 1})
q.put([3, 3])

print(q.full())
print(q.get())
print(q.get())
print(q.get())
print(q.empty())
print(q.full())
