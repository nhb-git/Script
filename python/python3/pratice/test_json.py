# -*- coding: utf-8 -*-
import os
import json

basedir = os.path.dirname(os.path.realpath(__file__))

# python字典对象转换为json对象
data = {
    'no': 1,
    'name': 'nhb',
    'url': 'http://www.baidu.com'
}

json_str = json.dumps(data)
print('python原始数据: ', repr(data))
print('json对象 ', json_str)

# json对象转为python字典对象
data2 = json.loads(json_str)
print("data2['name']: ", data2['name'])

# 写入json数据
file_path = os.path.join(basedir, 'file.json')
print(file_path)
with open(file_path, 'w') as f:
    json.dump(data, f)
