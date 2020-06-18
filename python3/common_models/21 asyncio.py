#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：6/17/2020  8:12 AM 
# 文件名称   ：21 asyncio.py
import asyncio
import threading


# 异步io 测试
# @asyncio.coroutine
# def hello():
#     print('hello world! %s' % threading.currentThread())
#     r = yield from asyncio.sleep(2)
#     print('hello again! %s' % threading.currentThread())
#
#
# look = asyncio.get_event_loop()
# tasks = [hello(), hello()]
# look.run_until_complete(asyncio.wait(tasks))
# look.close()


# 获取新浪、搜狐、163网站的首页
@asyncio.coroutine
def wget(host):
    print('wget host %s' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
        # Ignore the body, close the socket
    writer.close()


loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
