#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：6/16/2020  10:59 PM 
# 文件名称   ：19 re.py
import re


mail = 'niuhai@163.com'
# re_obj = re.match(r'^(\w*)\.?\w*@[0-9A-Za-z]+.(com|cn|edu)$', mail)
# if re_obj:
#     # 贪婪匹配，打印结果是('niuhai', 'com')
#     print(re_obj.groups())

# 预编译
# compile_obj = re.compile(r'^(\w*)\.?\w*@[0-9A-Za-z]+.(com|cn|edu)$')
# r = compile_obj.match(mail)
# print(r.groups())
s = 'test niu,hai ok, 33'
print(re.split(r'[ ,]', s))
