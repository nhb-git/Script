#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：6/18/2020  5:49 PM 
# 文件名称   ：ips.py
import asyncio


async def get_ip(file):
    try:
        l = []
        with open(file) as f:
            for line in f:
                l.append(line)
        return l
    except FileNotFoundError:
        print('file not exists')


# @asyncio.coroutine
async def get_ip_str(file):
    print('start exec ...')
    source_ip = await get_ip(file)
    print(';'.join([ip.strip() for ip in source_ip]))


loop = asyncio.get_event_loop()
loop.run_until_complete(get_ip_str('ips'))
loop.close()
