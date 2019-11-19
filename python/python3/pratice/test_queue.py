# -*- coding: utf-8 -*-
"""
测试进程间通讯队列
"""

import os
import time
import random
from multiprocessing import Process, Queue


def write(q):
    """
    向队列中写入数据
    """
    print("Process to write {0}.".format(os.getpid()))
    for value in ['A', 'B', 'C']:
        print("Put {0} to queue.".format(value))
        q.put(value)
        time.sleep(random.random())


def read(q):
    """
    读取队列中的数据
    """
    print("Process to read {0}".format(os.getpid()))
    while True:
        value = q.get(True)
        print("Get %s from queue" % value)


if __name__ == "__main__":
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()
