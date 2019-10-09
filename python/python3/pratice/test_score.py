# -*- coding: utf-8 -*-
'''
@file: test_score.py
@author: niuhaibao
'''
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def sanitize(time_string):
    '''转换时间值格式为 min:sec 的格式
    '''
    if '-' in time_string:
        splitter = '-'
        (mins, secs) = time_string.split(splitter)
    elif ':' in time_string:
        splitter = ':'
        (mins, secs) = time_string.split(splitter)
    else:
        return time_string
    return mins + '.' + secs


def get_times(times_file):
    '''From file get times value of person.
    '''
    try:
        with open(times_file) as data:
            times = data.readline()
        return (times.strip().split(','))
    except IOError as ioerr:
        print('File Error: ' + str(ioerr))
        return None


james_score = get_times('james.txt')
julie_score = get_times('julie.txt')
sarah_score = get_times('mikey.txt')
mikey_score = get_times('sarah.txt')

james_score = sorted(
    set([sanitize(score) for score in james_score]), reverse=True
)
julie_score = sorted(
    set([sanitize(score) for score in julie_score]), reverse=True
)
mikey_score = sorted(
    set([sanitize(score) for score in mikey_score]), reverse=True
)
sarah_score = sorted(
    set([sanitize(score) for score in sarah_score]), reverse=True
)

print(james_score[0:3])
print(julie_score[0:3])
print(mikey_score[0:3])
print(sarah_score[0:3])
