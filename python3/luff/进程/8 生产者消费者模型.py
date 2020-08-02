#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：8/2/2020  3:55 PM 
# 文件名称   ：8 生产者消费者模型.py
import time
from multiprocessing import Process, Queue, current_process, JoinableQueue


def producer(q):
    for message_num in range(10):
        time.sleep(0.5)
        message = current_process().name + '消息%s' % message_num
        q.put(message)
        print('生产了' + message)
    q.join()


def consumer(q):
    while True:
        time.sleep(1)
        message = q.get()
        q.task_done()
        print('消费了' + message)


if __name__ == '__main__':
    # 创建队列
    # q = Queue()
    q = JoinableQueue()

    # 创建生产者进程对象
    p1 = Process(target=producer, args=(q,))
    p2 = Process(target=producer, args=(q,))
    p3 = Process(target=producer, args=(q,))

    # 创建消费者进程对象
    c1 = Process(target=consumer, args=(q,))
    c2 = Process(target=consumer, args=(q,))
    c1.daemon = True
    c2.daemon = True

    # 请求操作系统创建生产者和消费者进程
    p1.start()
    p2.start()
    p3.start()
    c1.start()
    c2.start()
    p1.join()
    p2.join()
    p3.join()
    print('主')
