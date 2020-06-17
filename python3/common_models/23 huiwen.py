#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：6/17/2020  6:03 PM 
# 文件名称   ：23 huiwen.py



s = 'abccba'
s1 = 'abcd'


def huiwen(s_str):
    return s_str == s_str[::-1]


print(huiwen(s))
print(huiwen(s1))
