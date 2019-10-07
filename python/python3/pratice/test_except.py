# -*- coding: utf-8 -*-
'''
@file: test_except.py
@email:  niuhaibao@gmail.com
'''
import pickle


try:
    with open('missing.txt', 'wb') as data:
        pickle.dump(data, man_file)
except IOError as err:
    print('file error: ' + str(err))
except pickle.PickleError as perr:
    print('pickleing error: ' + str(perr))
