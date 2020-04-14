import time
from multiprocessing import Process, Lock


def work(name, lock):
    lock.acquire()
    print('%s 1' % (name,))
    time.sleep(3)
    print('%s 2' % (name,))
    time.sleep(3)
    print('%s 3' % (name,))
    lock.release()


if __name__ == '__main__':
    mexlock = Lock()
    for i in range(0, 3):
        p = Process(target=work, args=('task%s' % (i,), mexlock))
        p.start()
