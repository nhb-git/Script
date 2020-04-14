from multiprocessing import Process


N = 100


def work():
    global N
    N = 0
    print('子进程 %s' % N)


if __name__ == '__main__':
    p = Process(target=work, name='work1')
    p.start()
    p.join()
    print('主进程 %s' % N)
