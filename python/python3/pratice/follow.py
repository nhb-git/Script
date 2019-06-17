# -*- coding: utf-8 -*-
# follow.py
#
# Follow a file like tail -f.
import time


def follow(thefile):
    thefile.seek(0, 2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line


if __name__ == '__main__':
    logfile = open(r"D:\github\Script\python\python3\pratice\test.txt", "r")
    loglines = follow(logfile)
    for line in loglines:
        print(line, end='')
