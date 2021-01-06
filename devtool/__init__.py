'''
lanhuage: python
Descripttion: 
version: beta
Author: xiaoshuyui
Date: 2021-01-06 08:29:18
LastEditors: xiaoshuyui
LastEditTime: 2021-01-06 11:22:38
'''
__version__ = '0.0.0'
__caches__ = []

from functools import wraps


def testWrapper(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print('This is a test wrapper.')
        print(func.__annotations__)
        print(func.__qualname__)
        return func(*args, **kwargs)
    return inner


def isWrapped(func):
    @wraps(func)
    def inner(*args, **kwargs):
        global __caches__
        __caches__.append([func.__name__])
        print(func.__name__ + ' is cached.')
        func.__annotations__['wrapped_cached'] = True
        return func(*args, **kwargs)
    return inner
