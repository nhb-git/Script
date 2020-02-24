#! -*- coding: utf-8 -*-
"""
filename: server.py
author: niu
"""

import socket
import requests


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 8080))
s.listen(5)
print('start...')
res = s.accept()
print(res)
