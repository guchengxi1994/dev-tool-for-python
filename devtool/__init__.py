'''
lanhuage: python
Descripttion: 
version: beta
Author: xiaoshuyui
Date: 2021-01-06 08:29:18
LastEditors: xiaoshuyui
LastEditTime: 2021-01-06 16:58:24
'''
__version__ = '0.0.0'
__appname__ = 'DevTool'

from functools import wraps


class FuncAndName:
    def __init__(self, funcName: str, func, info: str = ''):
        self.funcName = funcName
        self.func = func
        self.info = info

    def __hash__(self) -> int:
        return hash(self.funcName)

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, self.__class__):
            return False
        return self.funcName == o.funcName

    def __str__(self):
        return self.funcName


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
        print(func.__name__ + ' is cached.')
        func.__annotations__['wrapped_cached'] = True
        return func(*args, **kwargs)

    return inner


def infoDecorate(message: str = '', **infomation):
    def decorator(func):
        @wraps(func)
        def sub_dec(*args, **kwargs):
            return func(*args, **kwargs)

        return sub_dec

    return decorator
