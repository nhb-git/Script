#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：7/30/2020  8:02 PM 
# 文件名称   ：1 开启子进程的方式.py
import os
import time
import random
from time import ctime
from multiprocessing import Process, Pool, current_process


# 方式1
# def task(name):
#     print('%s is running' % name)
#     time.sleep(3)
#     print('%s is done' % name)
#
#
# if __name__ == '__main__':
#     # Process(target=task, kwargs={'name': '子进程1'})
#     p = Process(target=task, args=('子进程1',))
#     p.start()   # 给操作系统发送信号创建进程
#     print('主')

# 方式2
# class MyProcess(Process):
#     def __init__(self, name):
#         super(MyProcess, self).__init__()
#         self.name = name
#
#     def run(self):
#         print('%s is running' % self.name)
#         time.sleep(3)
#         print('%s is done' % self.name)
#
#
# if __name__ == '__main__':
#     p = MyProcess('子进程1')
#     p1 = MyProcess('子进程2')
#     p.start()
#     p1.start()

# 进程池
def task(name):
    print('start task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    print('end task %s runs %0.2f seconds.' % (name, (time.time() - start)))
    return current_process().name + 'done'


if __name__ == '__main__':
    print('parent process %s.' % os.getpid())

    result = []

    p = Pool()  # 初始化进程池
    for i in range(5):
        result.append(p.apply_async(task, args=(i,)))  # 追加任务 apply_async 是异步非阻塞的，就是不用等待当前进程执行完毕，随时根据系统调度来进行进程切换。

    p.close()

    p.join()  # 等待所有结果执行完毕

    for res in result:
        print(res.get())  # get()函数得出每个返回结果的值

    print(f'all done at: {ctime()}')
    print(type(ctime()))
