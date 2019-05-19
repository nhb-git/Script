# -*- coding: utf-8 -*-
import os


file_log = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), 'access.log'
    )
d = {}
with open(file_log) as f:
    for line in f:
        key = line.split()[8]
        d.setdefault(key, 0)
        d[key] += 1

sum_requests = 0
error_requests = 0

for key, val in d.items():
    if int(key) >= 400:
        error_requests += val
    sum_requests += val

print('error rate: {0:.2f}%'.format(error_requests * 100.0 / sum_requests))