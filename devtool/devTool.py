'''
lanhuage: python
Descripttion: 
version: beta
Author: xiaoshuyui
Date: 2021-01-06 08:26:44
LastEditors: xiaoshuyui
LastEditTime: 2021-01-06 16:54:42
'''
import importlib
import os

from devtool.utils.getFunctions import find_functions
from devtool.utils.getModules import find_modules
from devtool.utils.logger import logger


class DevTool:
    storage = []

    @classmethod
    def do(cls, moduleName=''):
        print('<================ Init... ================>')
        try:
            module = importlib.__import__(moduleName)
            # print(module.__name__)
            modulePath = os.path.dirname(module.__file__)
            sub_modules = find_modules(modulePath)
            # print(sub_modules)
            member_list = find_functions(sub_modules, moduleName)
            # print(member_list)
            for i in member_list:
                try:
                    i.func.__call__()
                    if i.func.__annotations__.get('wrapped_cached', False):
                        cls.storage.append(i)
                except:
                    continue
        except Exception as e:
            print(e)
        print('<================ finish ================>')
        print(cls.storage)

    @classmethod
    def grep(cls, grepType, *kwds):
        """
        grepType should be a str in ['and','or']
        """
        if len(cls.storage) == 0:
            print(
                'Nothing found. Plz run DevTool.go() first or just there is nothing to find.'
            )
        else:
            if grepType not in ['and', 'or']:
                logger.warning(
                    "grepType should be a str in ['and','or'],  but got {}, use 'or' instead."
                    .format(grepType))
                grepType = 'or'
