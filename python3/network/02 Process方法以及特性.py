import os
import time
from multiprocessing import Process


def task(name):
    print('task run ... %s, 进程id是%s, 父进程id是%s' % (name, os.getpid(), os.getppid()))
    time.sleep(3)
    print('task end ... %s, 进程id是%s, 父进程id是%s' % (name, os.getpid(), os.getppid()))


class MyProcess(Process):
    def __init__(self, name, time):
        super().__init__()
        self.name = name
        self.time = time

    def run(self):
        print('%s start 子进程 id %s, 父进程 id %s' % (self.name, os.getpid(), os.getppid()))
        time.sleep(self.time)
        print('%s end 子进程 id %s, 父进程 id %s' % (self.name, os.getpid(), os.getppid()))


if __name__ == '__main__':
    # 方式1
    # p = Process(target=task, args=('task1',))
    # p = Process(target=task, kwargs={'name': 'task1'})
    # p.start()
    # print('主进程id %s, 父进程id %s' % (os.getpid(), os.getppid()))
    # 方式2
    start_time = time.time()
    p = MyProcess('task1', 1)
    # p1 = MyProcess('task2', 5)
    # p2 = MyProcess('task3', 3)
    p.start()
    p.terminate()
    time.sleep(3)
    print(p.is_alive())
    print(p.name)
    # p.join()
    # p1.start()
    # p1.join()
    # p2.start()
    # p2.join()
    # print(time.time()-start_time)
    # print('主进程id %s, 父进程id %s' % (os.getpid(), os.getppid()))
