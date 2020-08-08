#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：8/7/2020  12:49 PM 
# 文件名称   ：asyncio模块.py
import asyncio


async def main():
    print('hello')
    await asyncio.sleep(1)
    print('world')


def run():
    cou = main()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(cou)
    loop.close()


run()
