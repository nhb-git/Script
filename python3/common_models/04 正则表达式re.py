import re


# re.findall() 将匹配到的内容放入列表中
phone_list = []
# with open('04 phone.txt', 'r', encoding='utf-8') as f:
    # phone_list = re.findall('[0-9]{6}', f.read())
    # re.match() 匹配字符串开头的内容是否符合正则
    # match_obj = re.match('[0-9]{3}', f.read())
    # phone_list = match_obj.group()
    #
    # search_obj = re.search('[0-9]{6}', f.read())
    # phone_list = search_obj.group()
# print(phone_list)

# \A，从字符串的开头匹配
# print(re.search(r'\Aabc', 'cabcd'))

# \Z, 从字符串的结尾匹配
# print(re.search(r'abc\Z', 'cabcc'))

# \d, 匹配数字
# print(re.search(r'\d{1,2}', '3ab'))

# \D, 匹配非数字
# print(re.search(r'\D', 'abcd3'))

# \w, 匹配a-zA-Z0-9
# print(re.search(r'\w', 'abA*9'))

# \s, 匹配空白字符
# print(re.search(r'\s', '\tn\t'))

# 分组命名匹配 (?P<name>reg)
r = re.search(r'(?P<city>\d{3})(?P<age>\d{2})', '22244')
print(r.group())
print(r.groups())
print(r.groupdict())
