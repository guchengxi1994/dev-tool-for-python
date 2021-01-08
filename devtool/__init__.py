'''
lanhuage: python
Descripttion: 
version: beta
Author: xiaoshuyui
Date: 2021-01-06 08:29:18
LastEditors: xiaoshuyui
LastEditTime: 2021-01-08 08:41:16
'''
__version__ = '0.0.0'
__appname__ = 'DevTool'

import logging
import os
import platform
from functools import wraps
import traceback

from concurrent_log_handler import ConcurrentRotatingFileHandler

__current_platform__ = platform.system()

del platform

BASE_DIR = os.path.abspath(os.curdir)
# print(BASE_DIR)

logit_logger = logging.getLogger(__appname__)
logit_logger.setLevel(level=logging.INFO)

if not os.path.exists(BASE_DIR + os.sep + "DevLog"):
    os.mkdir(BASE_DIR + os.sep + "DevLog")

LOG_PATH = BASE_DIR + os.sep + "DevLog" + os.sep + 'devlog.log'

rHandler = ConcurrentRotatingFileHandler(filename=LOG_PATH,
                                         maxBytes=5 * 1024 * 1024,
                                         backupCount=5)
rHandler.setLevel(logging.INFO)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
rHandler.setFormatter(formatter)

logit_logger.addHandler(rHandler)


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


def setWrap(func):
    @wraps(func)
    def inner(*args, **kwargs):
        # print(func.__name__ + ' is cached.')
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


def logit(func):
    @setWrap
    def execute(*args, **kwargs):
        try:
            func(*args, **kwargs)
            logit_logger.info(func.__module__ + '.' + func.__name__ +
                              ' finishes successfully.')
        except Exception:
            res = traceback.format_exc()
            logit_logger.error(func.__module__ + '.' + func.__name__ + " " +
                               res)

    return execute
