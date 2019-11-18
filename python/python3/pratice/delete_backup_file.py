# -*- coding: utf-8 -*-
"""
Delete backup file.
"""
import os
import glob
import shutil
import argparse
from collections import Counter


def _argparse():
    """获取命令行参数
    """
    parser = argparse.ArgumentParser(
        description="Delete backup file."
    )
    parser.add_argument(
        '-f', '--file', dest='file', required=True,
        help="'Include will delete file's list in the file."
    )
    parser.add_argument(
        '-v', '--version', default=1,
        help='Version info.'
    )
    return parser.parse_args()


def get_file_path():
    """从文件获取文件目录列表
    """
    try:
        parser = _argparse()
        file_name = parser.file
        with open(file_name) as f:
            for file_path in f:
                if os.path.exists(file_path):
                    yield file_path
    except FileNotFoundError:
        print('Please Check file is or not exist.')


def surpass_max_number(path, number=5):
    """检查目录下的文件或目录总数是否超过number设定
    """
    if os.path.isdir(path):
        full_path = os.path.join(path, '*')
        if len(glob.glob(full_path)) <= number:
            return False
        return True
    else:
        return False


def get_earliest_file(path):
    if os.path.isdir(path):
        full_path = os.path.join(path, '*')
    if full_path:
        d = dict()
        for each_path in glob.iglob(full_path):
            d[each_path] = os.path.getctime(each_path)
        print(d)
        path_list = Counter(d)
        return path_list.most_common()[-1][0]


def delete_file(path):
    """删除文件
    """
    try:
        if os.path.isdir(path):
            shutil.rmtree(path)
    except FileNotFoundError:
        print('File not found.')
