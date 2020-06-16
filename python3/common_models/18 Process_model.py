#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：6/16/2020  7:20 PM 
# 文件名称   ：process.py
import os
import random
import time
from multiprocessing import Process, Pool, Queue


def run_poc(name):
    print('run child process %s %s' % (name, os.getpid()))


# if __name__ == '__main__':
#     print('Parent pid %s' % os.getpid())
#     p = Process(target=run_poc, args=('test',))
#     print('child process will start...')
#     p.start()
#     p.join()
#     print('child process end...')

# 线程池
# if __name__ == '__main__':
#     print('Parent pid %s' % os.getpid())
#     p = Pool(4)
#     for process_id in range(10):
#         p.apply_async(run_poc, args=(process_id,))
#     print('process run start...')
#     p.close()
#     p.join()
#     print('process run end...')

# 队列
def write(q):
    print('Process to write %s' % os.getpid())
    messages = ['a', 'b', 'c']
    for message in messages:
        print('Put value %s to queue' % message)
        q.put(message)
        time.sleep(random.random())


def read(q):
    print('Process to read %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get value %s from queus' % value)


if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()

