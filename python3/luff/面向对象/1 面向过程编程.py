# -*- coding: utf-8 -*-
"""
面向过程：聚焦于解决问题的步骤，顺序是核心
优点：
1. 解决问题的步骤很明确
2. 大任务分解为小任务很容易

缺点:
1. 可扩展性差

应用场景：适用于不经常修复的场景
"""
import json


def interactive():
    """
    接收用户输入的账户名和密码
    """
    name = input(":>> ").strip()
    pwd = input(":>> ").strip()
    return {
        'name': name,
        'pwd': pwd
    }


def check(user_info):
    """
    检查账户名和密码是否符合要求
    :param user_info:
    :return:
    """
    is_valid = True
    if len(user_info['name']) == 0:
        print('用户名不能为空')
        is_valid = False
    if len(user_info['pwd']) < 6:
        print('密码不能小于6位')
        is_valid = False
    return {
        'is_valid': is_valid,
        'user_info': user_info
    }


def register(check_info):
    """
    用户信息写入文件
    :param check_info:
    :return:
    """
    if check_info['is_valid']:
        with open('db.json', 'w', encoding='utf-8') as f:
            json.dump(check_info['user_info'], f)


def main():
    user_info = interactive()
    check_info = check(user_info)
    register(check_info)


if __name__ == '__main__':
    main()

