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
            line = data.readline()
        templ = line.strip().split(',')
        return ({
            'name': templ.pop(0),
            'dob': templ.pop(0),
            'times': str(
                sorted(
                    set([sanitize(score) for score in templ]), reverse=True
                )[0:3]
            )
        })
    except IOError as ioerr:
        print('File Error: ' + str(ioerr))
        return None


james = get_times('james.txt')
print(james['name'] + "'s fastest times are: " + str(james['times']))

julie = get_times('julie.txt')
print(julie['name'] + "'s fastest times are: " + str(julie['times']))

sarah = get_times('mikey.txt')
print(sarah['name'] + "'s fastest times are: " + str(sarah['times']))

mikey = get_times('sarah.txt')
print(mikey['name'] + "'s fastest times are: " + str(mikey['times']))
