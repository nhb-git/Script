#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：7/30/2020  10:20 PM 
# 文件名称   ：3 Process对象的其他对象和方法.py
import os
import time
from multiprocessing import Process


def task():
    print('pid is running')
    time.sleep(3)
    print('pid is done')
    print(os.getpid())
#
#
# if __name__ == '__main__':
#     p = Process(target=task)
#     p.start()
#     p.join()
#     print('主')
#     print(p.pid)


# 并发执行
# if __name__ == '__main__':
#     start_time = time.time()
#     p1 = Process(target=task)
#     p2 = Process(target=task)
#     p3 = Process(target=task)
#     p_l = [p1, p2, p3]
#     for p in p_l:
#         p.start()
#
#     for p in p_l:
#         p.join()
#
#     print('主')
#     print(time.time() - start_time)

# 串行执行
# if __name__ == '__main__':
#     start_time = time.time()
#     p1 = Process(target=task)
#     p2 = Process(target=task)
#     p3 = Process(target=task)
#     p1.start()
#     p1.join()
#     p2.start()
#     p2.join()
#     p3.start()
#     p3.join()
#     print(time.time()-start_time)

# 了解
if __name__ == '__main__':
    p = Process(target=task, name='p1')
    print(p.is_alive())
    p.start()
    print(p.is_alive())     # 检测p进程是否存活
    p.terminate()
    time.sleep(3)
    print(p.is_alive())
    print(p.name)
