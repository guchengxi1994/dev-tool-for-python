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
    currentModulePath = ''

    @classmethod
    def do(cls, moduleName=''):
        print('<================ Init... ================>')
        module = importlib.__import__(moduleName)
        modulePath = os.path.dirname(module.__file__)
        sub_modules = find_modules(modulePath)
        member_list = find_functions(sub_modules, moduleName)
        for i in member_list:
            try:
                i.func.__call__()
                if i.func.__annotations__.get('wrapped_cached', False):
                    cls.storage.append(i)
            except:
                continue
        print('<================ finish ================>')
        cls.currentModulePath = modulePath

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

    @classmethod
    def tree(cls, moduleName):
        if cls.currentModulePath == '':
            module = importlib.__import__(moduleName)
            modulePath = os.path.dirname(module.__file__)
        else:
            modulePath = cls.currentModulePath

        for root, dirs, files in os.walk(modulePath):
            level = root.replace(modulePath, '').count(os.sep)
            dir_indent = "|   " * (level - 1) + "|-- "
            file_indent = "|   " * level + "|-- "
            if not level:
                print('.')
            else:
                tmp = os.path.basename(root)
                if tmp != '__pycache__':
                    print('{}{}'.format(dir_indent, os.path.basename(root)))
                del tmp
            for f in files:
                tmp = root + os.sep + f
                if not f.endswith('.pyc'):
                    print('{}{}'.format(file_indent, f))
