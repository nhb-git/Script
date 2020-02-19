# -*- coding: utf-8 -*-
import copy
s = {'niu': 1, 'hai': 2, 'bao':{'1': 1, '2': 2}}
s1 = s.copy()
print(s)
print(s1)
s1['bao']['1'] = 3
print(s)
print(s1)
s2 = copy.deepcopy(s)
s2['bao']['1'] = 4
print(s)
print(s2)
