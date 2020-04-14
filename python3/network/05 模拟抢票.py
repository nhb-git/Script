import time
import json
from multiprocessing import Process, Lock


def search(name):
    time.sleep(1)
    with open('db.txt', 'r', encoding='utf-8') as f:
        dic = json.load(f)
    print('%s 查的余票: %s' % (name, dic['count']))


def get(name):
    time.sleep(3)
    with open('db.txt', 'r', encoding='utf-8') as f:
        dic = json.load(f)
    if dic['count'] > 0:
        dic['count'] -= 1
        with open('db.txt', 'w', encoding='utf-8') as f:
            json.dump(dic, f)
        print('%s 购票成功' % (name,))


def work(name, lock):
    search(name)
    lock.acquire()
    get(name)
    lock.release()


if __name__ == '__main__':
    metux = Lock()
    for i in range(10):
        p = Process(target=work, args=('用户 %s' % i, metux))
        p.start()
