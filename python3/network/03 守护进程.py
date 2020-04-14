import time
from multiprocessing import Process


def work(name):
    print('%s running...' % (name,))
    p = Process(target=time.sleep, args=(3,))
    p.start()


if __name__ == '__main__':
    p = Process(target=work, args=('work1',))
    # p.daemon = True
    p.start()
    p.join()
    print('主进程')
