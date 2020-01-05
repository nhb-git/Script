# -*- coding: utf-8 -*-
"""
测试多进程模块
"""

import os
import glob
import shutil
from multiprocessing import Process, Pool


def run_proc(name):
    """Print process pid.
    """
    print('Run child process {0} ({1})...'.format(name, os.getpid()))


def process():
    print('Parent process {0}'.format(os.getpid()))
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')


def get_filelist(path):
    path = os.path.join(path, '*')
    file_list = ','.join(glob.glob(path))
    print(file_list)
    print('Child process {0} ({1})'.format(file_list, os.getpid()))


def delete_dir(path):
    try:
        shutil.rmtree(path)
        print('Child process {0} ({1})'.format(path, os.getpid()))
    except FileNotFoundError:
        print('error')


def mul_pool():
    print('Parent process {0}'.format(os.getpid()))
    p = Pool(2)
    with open('/tmp/test') as f:
        for line in f:
            p.apply_async(delete_dir, args=(line.strip(),))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')


if __name__ == "__main__":
    # process()
    mul_pool()
