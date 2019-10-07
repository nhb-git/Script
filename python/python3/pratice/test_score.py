# -*- coding: utf-8 -*-
'''
@file: test_score.py
@author: niuhaibao
'''
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
        (mins, secs) = time_string.split(splitter)
    elif ':' in time_string:
        splitter = ':'
        (mins, secs) = time_string.split(splitter)
    else:
        return time_string
    return mins + '.' + secs


james_score = []
julie_score = []
sarah_score = []
mikey_score = []

try:
    with open('james.txt') as james_data:
        line = james_data.readline()
        james_score = line.strip().split(',')
except FileNotFoundError as ferr:
    print('File Error: ' + str(ferr))

try:
    with open('julie.txt') as julie_data:
        line = julie_data.readline()
        julie_score = line.strip().split(',')
except FileNotFoundError as ferr:
    print('File Error: ' + str(ferr))

try:
    with open('mikey.txt') as mikey_data:
        line = mikey_data.readline()
        mikey_score = line.strip().split(',')
except FileNotFoundError as ferr:
    print('File Error: ' + str(ferr))

try:
    with open('sarah.txt') as sarah_data:
        line = sarah_data.readline()
        sarah_score = line.strip().split(',')
except FileNotFoundError as ferr:
    print('File Error: ' + str(ferr))

new_james = []
new_julie = []
new_mikey = []
new_sarah = []

new_james = [sanitize(score) for score in james_score]
new_julie = [sanitize(score) for score in julie_score]
new_mikey = [sanitize(score) for score in mikey_score]
new_sarah = [sanitize(score) for score in sarah_score]

print(sorted(new_james, reverse=True))
print(sorted(new_julie, reverse=True))
print(sorted(new_mikey, reverse=True))
print(sorted(new_sarah, reverse=True))
