#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：8/3/2020  12:10 PM 
# 文件名称   ：3 gevent并发套接字通信-客户端.py
from socket import *
from threading import currentThread, Thread


def client():
    client = socket(AF_INET, SOCK_STREAM)
    client.connect(('127.0.0.1', 8090))

    while True:
        client.send(('%s hello' % currentThread().getName()).encode('utf-8'))
        data = client.recv(1024)
        print(data.decode('utf-8'))
    client.close()


if __name__ == '__main__':
    for i in range(1000):
        t = Thread(target=client)
        t.start()
