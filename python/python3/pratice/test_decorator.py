# -*- coding: utf-8 -*-
"""
function: test decorator
filename: test_decorator
author: haibao
"""
import time
from functools import wraps


def a_new_decorator(func):
    @wraps(func)
    def wrap_function():
        print("I am doing some boring work before executing a_func()")
        func()
        print("I am doing some boring work after executing a_func()")
    return wrap_function


def a_args_new_decorator(arg):
    def decorator(func):
        @wraps(func)
        def wrap_function(*args, **kwargs):
            print("exec start: %s" % (
                time.strftime("%Y-%m-%d %l:%M:%S %p", time.localtime()))
            )
            print(arg)
            func(*args, **kwargs)
            print(
                "exec end: {0}".format(
                    time.strftime("%Y-%m-%d %l:%M:%S %p", time.localtime())
                )
            )

        return wrap_function

    return decorator


def print_exec_time(func):
    @wraps(func)
    def wrap_function():
        print(
            'script start exec time: %s' % time.strftime(
                "%Y-%m-%d %H:%M:%S", time.localtime()
            )
        )
        func()
        print(
            'script end exec time: %s' % time.strftime(
                "%Y-%m-%d %H:%M:%S", time.localtime()
            )
        )
    return wrap_function


# @a_new_decorator
# @print_exec_time
@a_args_new_decorator('hello world')
def func_require_decorator(name):
    time.sleep(10)
    print(name)
    print('I require decorator')


func_require_decorator('niuhaibao')
