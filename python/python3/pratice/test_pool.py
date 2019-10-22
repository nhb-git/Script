# -*- coding: utf-8 -*-
import os
import time
import random
from multiprocessing import Pool


def to_work(num):
    # print process num
    print("----start %d, Process's pid is %d, parant's pid is %d---" % (
        num, os.getpid(), os.getppid()
        )
    )

    # delay time
    time.sleep(random.random())
    print("%d num process done %d 1 task." % (os.getpid(), num))

    time.sleep(random.random())
    print("%d num process done %d 2 task." % (os.getpid(), num))

    time.sleep(random.random())
    print("%d num process done %d 3 task." % (os.getpid(), num))

    time.sleep(random.random())
    print('-----task end----%d' % (num))


def main():
    # create Process pool with max three num
    process_num = 3
    po = Pool(process_num)
    for i in range(1, 5):
        po.apply_async(to_work, (i,))
    print("----start-----")
    po.close()
    po.join()
    print('------end--------------')


if __name__ == "__main__":
    main()
