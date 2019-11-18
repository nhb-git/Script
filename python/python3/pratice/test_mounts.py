# -*- coding: utf-8 -*-
"""
Read /proc/mounts files content.
"""
from collections import namedtuple


mount = namedtuple(
    'mount_point', [
        'one', 'two', 'three', 'four', 'five', 'six'
    ]
)


def get_mount_info():
    with open('/proc/mounts') as f:
        for line in f:
            print(mount(*(line.split()))[0])


if __name__ == '__main__':
    get_mount_info()
