'''
lanhuage: python
Descripttion: 
version: beta
Author: xiaoshuyui
Date: 2021-01-06 08:29:18
LastEditors: xiaoshuyui
LastEditTime: 2021-01-08 17:24:29
'''
__version__ = '0.0.0'
__appname__ = 'DevTool'

import logging
import os
import platform
from functools import wraps
import traceback
import pickle

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
Cache_path = BASE_DIR + os.sep + "DevLog" + os.sep + 'devCache.dump'

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


def do_nothing():
    pass


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
        @setWrap
        @wraps(func)
        def sub_dec(*args, **kwargs):
            func.__annotations__[
                'message'] = message if message != '' else do_nothing

            if len(infomation) > 0:
                for k, v in infomation.items():
                    func.__annotations__[k] = v
            return func(*args, **kwargs)

        return sub_dec

    return decorator


def logit(**params):
    def decorator(func):
        @setWrap
        def execute(*args, **kwargs):
            flag = False
            save = params.get('save', False)
            load = params.get('load', False)
            if load and os.path.exists(Cache_path):
                with open(Cache_path, 'rb') as fi:
                    d = pickle.load(fi)
                    if func.__module__ + '.' + func.__name__ in d.keys():
                        res = d[func.__module__ + '.' + func.__name__]
                        return res
                    else:
                        flag = True
            if not flag:
                try:
                    res = func(*args, **kwargs)
                    logit_logger.info(func.__module__ + '.' + func.__name__ +
                                      ' finishes successfully.')
                    if save:
                        d = dict()
                        d[func.__module__ + '.' + func.__name__] = res
                        # fan = FuncAndName(func.__module__ + '.' + func.__name__,None,'',res)
                        if not os.path.exists(Cache_path):
                            with open(Cache_path, 'wb') as fi:
                                pickle.dump(d, fi)
                        else:
                            with open(Cache_path, 'rb') as fi:
                                d = pickle.load(fi)
                                d[func.__module__ + '.' + func.__name__] = res
                                pickle.dump(d, fi)

                except Exception:
                    # res = traceback.format_exc()
                    logit_logger.error(func.__module__ + '.' + func.__name__ +
                                       " " + traceback.format_exc())
                    res = None
                return res

        return execute

    return decorator


def Test(*pas, **params):
    def decorator(func):
        @logit()
        def execute(*args, **kwargs):
            if len(pas) == len(func.__code__.co_varnames):
                args = pas
            if len(params) > 0:
                for k, v in params.items():
                    if k in func.__code__.co_varnames:
                        kwargs[k] = v
            return func(*args, **kwargs)

        return execute

    return decorator
