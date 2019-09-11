# -*- coding: utf-8 -*-
def create_counter():
    def f():
        i = 0
        while True:
            i += 1
            yield i
    it = f()

    def counter():
        return next(it)
    return counter


counter1 = create_counter()
print(counter1())
print(counter1())
