# -*- coding: utf-8 -*-
# def g_test():
#     while True:
#         n = yield
#         print('recv %s' % n)
#
#
# g = g_test()
#
# # 调用生成器,并给生成器发送None到yield
# g.__next__()
#
#
# g.send(None)
# for i in range(10):
#     g.send(i)


def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('consumer %s' % n)
        r = '200 ok'


def producer(c):
    c.send(None)
    n = 0
    while n < 5:
        n += 1
        print('producer %s' % n)
        r = c.send(n)
        print('producer revc consumer %s' % r)
    c.close()


c = consumer()
producer(c)
