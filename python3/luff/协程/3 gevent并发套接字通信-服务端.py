#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：8/3/2020  12:10 PM 
# 文件名称   ：3 gevent并发套接字通信-服务端.py
from gevent import monkey, spawn; monkey.patch_all()
from socket import *


def communicate(conn):
    while True:
        try:
            data = conn.recv(1024)
            if not data: break
            conn.send(data.upper())
        except ConnectionRefusedError:
            break
    conn.close()


def server(ip, port):
    server = socket(AF_INET, SOCK_STREAM)
    server.bind((ip, port))
    server.listen(50000)

    while True:
        conn, addr = server.accept()
        spawn(communicate, conn)
    server.close


if __name__ == '__main__':
    g = spawn(server, '127.0.0.1', 8090)
    g.join()
