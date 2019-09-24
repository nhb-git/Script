# -*- coding: utf-8 -*-
import os


current_dir = os.path.abspath('.')
print(os.path.split(current_dir))
os.mkdir(os.path.join(current_dir, 'test123'))
