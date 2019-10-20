# -*- coding: utf-8 -*-
"""
@filename: test_class.py
@author: haibao
"""


class Athlete():
    def __init__(self, a_name, a_dob=None, a_times=[]):
        self.name = a_name
        self.dob = a_dob
        self.times = a_times

    def top3(self):
        pass

    def add_time(self, extr_time):
        """Add a times value to source times.
        """
        self.times.append(extr_time)

    def add_times(self, list_times):
        """Add time's list to source times
        """
        self.times.extend(list_times)
