#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：6/16/2020  9:06 PM 
# 文件名称   ：subprocess1.py
import subprocess


# 无输入
# print('$ nslookup www.baidu.com')
# r = subprocess.call(['nslookup', 'www.baidu.com'])
# r = subprocess.call(['telnet', 'www.baidu.com', '80'])
# print('exit code:', r)

# 有输入
print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\nbaidu.com\nexit\n')
print('---')
print(output.decode('utf-8'))
print('return code:', p.returncode)
