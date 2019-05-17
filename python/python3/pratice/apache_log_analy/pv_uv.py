# -*- coding: utf-8 -*-
import os


log_file = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'access.log'
    )
ips = []
with open(log_file, 'r') as f:
    for line in f:
        ips.append(line.split()[0])
print("PV is {0}".format(len(ips)))
print("UV is {0}".format(len(set(ips))))
