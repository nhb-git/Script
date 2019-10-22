# -*- coding: utf-8 -*-
import os
import time
import random


def work(pid):
    if pid == 0:
        print('child process %d start exec, parent process %d' % (
            os.getpid(), os.getppid()
            )
        )
        time.sleep(random.random())
        print('one')
        time.sleep(random.random())
        print('two')
        time.sleep(random.random())
        print('----child process end----------')
    else:
        print('Parent process start exec, pid is %d, Parent Parent pid is %d' % (
            os.getpid(), os.getppid()
            )
        )
        time.sleep(random.random())
        print('parent one')
        time.sleep(random.random())
        print('parent two')
        time.sleep(random.random())
        print('Parent process end')


def main():
    pid = os.fork()
    work(pid)


if __name__ == "__main__":
    main()
