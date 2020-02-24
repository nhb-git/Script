#! -*- coding: utf-8 -*-
"""
filename: client.py
author: niu
"""

import socket


c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(('127.0.0.1', 8080))
