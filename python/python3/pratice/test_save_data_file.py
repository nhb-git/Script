# -*- coding: utf-8 -*-

"""
test_save_data_file.py
~~~~~~~~~~~~~~~~~~~~~~

Save data to file.
"""


import os


print(os.path.dirname(__file__))
man = []
other = []
try:
    os.chdir(os.path.dirname(__file__))
    data = open('1.txt', 'w')
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass
    data.close()
except IOError:
    print('The datafile if missing!')

try:
    man_data = open('man_data.txt', 'w+')
    other_data = open('other_data.txt', 'w')
    print(man, man_data)
    print(other, other_data)
except IOError:
    print('File Error.')
finally:
    if 'man_data' in locals():
        man_data.close()
    if 'other_data' in locals():
        other_data.close()
