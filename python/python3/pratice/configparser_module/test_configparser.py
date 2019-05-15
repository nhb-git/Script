# -*- coding: utf-8 -*-
import configparser


cp = configparser.ConfigParser(allow_no_value=True)
cp.read('my.cnf')
cp.sections()
