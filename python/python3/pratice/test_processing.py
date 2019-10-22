# -*- coding: utf-8 -*-
import os
from multiprocessing import Process


print('Process ({}) start...'.format(os.getpid()))

# Only works on Unix/Linux/Mac:
pid = os.fork()
if pid == 0:
    print(
        'I am child process ({}) and my parent is {}.'.format(
            os.getpid(), os.getppid()
        )
    )
else:
    print('I ({}) just created a child process ({}).'.format(os.getpid(), pid))


def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))


if __name__ == "__main__":
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')
