# -*- coding: utf-8 -*-
import re


# re.split() 以正则匹配到的字符串作为分隔符，返回列表
# print(re.split(r'a', 'bcadeamn'))
# print(re.split(r'[0-9]{2}', 'ab34bc3mn56ie'))

# re.sub()  用新字符串替换正则匹配到的字符串并替换
# print(re.sub(r'abc', 'ABC', '12abcABCabc', count=1))

# re.fullmatch() 完全匹配字符串, 可以校验某一完整字符串是否符合正则规范
# print(re.fullmatch(r'[0-9]{2}', '22'))

# re.compile() 编译正则匹配规则，提高匹配效率
# re_c = re.compile(r'[0-9]{2}')
# print(re_c.search('ab23cd'))

# flag, re.I,   忽略大小写
# print(re.search(r're', 'abRec', flags=re.I))

# re.M, 默认是单行字符串匹配，re.M开启多行匹配的功能，影响行首^和行尾$的匹配
# print(re.search(r'^ab', 'cd\nab', re.M))

# re.S 改变.的功能，使其能匹配任何字符
# print(re.search(r'.', '\n'))
# print(re.search(r'.', '\n', re.S))
# print(re.split('[+*]', 'sb+mb*l'))

# 验证邮箱是否合法
print(re.fullmatch(r'\w+@\w+\.(com|cn|edu)', 'niuhaibaovip@163.com'))
