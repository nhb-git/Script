# -*- coding: utf-8 -*-
class MonthConver:
    regex = "[0-9]{2}"

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return '%2d' % value
