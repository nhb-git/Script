# -*- coding: utf-8 -*-
def hanio(n, a, b, c):
    if n > 0:
        hanio(n-1, a, c, b)
        print('move from %s to %s' % (a, c))
        hanio(n-1, b, a, c)


hanio(2, 'A', 'B', 'C')
