# -*- coding: utf-8 -*-
import os
from collections import Counter

file_log = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), 'access.log'
    )
c = Counter()
with open(file_log) as f:
    for line in f:
        c[line.split()[6]] += 1
print('Popular resource: {0}'.format(c.most_common(2)))
