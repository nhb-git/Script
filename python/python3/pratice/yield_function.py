# -*- coding: utf-8 -*-
import time


def print_list(value):
    sum = 0
    for i in range(value):
        sum += i
        yield sum


if __name__ == "__main__":
    p = print_list(10)
    for i in p:
        print(i)
        time.sleep(2)
