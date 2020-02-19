def register(name, age, major='cs', country='cn', *args, **kwargs):
    print('name:{0} age:{1} major:{2} country:{3}'.format(name, age, major, country))
    print(args)
    print(kwargs)


def args_test(major='cs', *args, **kwargs):
    print(kwargs)
    print(args)


register('hai', 30)
register(name='niu', age=30, country='us')
