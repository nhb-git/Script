# -*- coding: utf-8 -*-
"""
Monitor disk data.
"""
import os
from __future__ import print_function
from collections import namedtuple


Disk = namedtuple(
    'Disk', 'major_number minor_number device_name'
    ' read_count read_merged_count read_sections'
    ' time_spent_reading write_count write_merged_count'
    ' write_sections time_spent_write io_requests'
    ' time_spent_doing_io weighted_time_spent_doing_io'
)


def get_disk_info(device):
    """From /proc/diskstats file get disk info.
    """
    with open('/proc/diskstats') as f:
        for line in f:
            if line.split()[2] == device:
                return Disk(*(line.split()))