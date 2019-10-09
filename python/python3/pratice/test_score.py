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

james_score = sorted([sanitize(score) for score in james_score], reverse=True)
julie_score = sorted([sanitize(score) for score in julie_score], reverse=True)
mikey_score = sorted([sanitize(score) for score in mikey_score], reverse=True)
sarah_score = sorted([sanitize(score) for score in sarah_score], reverse=True)

unique_james = list()
unique_julie = list()
unique_mikey = list()
unique_sarah = list()

for each in james_score:
    if each not in unique_james:
        unique_james.append(each)

for each in julie_score:
    if each not in unique_julie:
        unique_julie.append(each)

for each in mikey_score:
    if each not in unique_mikey:
        unique_mikey.append(each)

for each in sarah_score:
    if each not in unique_sarah:
        unique_sarah.append(each)

print(unique_sarah[0:3])
print(unique_james[0:3])
print(unique_julie[0:3])
print(unique_mikey[0:3])
