#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：6/17/2020  8:12 AM 
# 文件名称   ：21 asyncio.py
import asyncio


@asyncio.coroutine
def hello():
    print('hello world!')
    r = yield from asyncio.sleep(1)
    print('hello again!')
