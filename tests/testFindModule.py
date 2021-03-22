'''
lanhuage: python
Descripttion: 
version: beta
Author: xiaoshuyui
Date: 2021-01-06 11:36:12
LastEditors: xiaoshuyui
LastEditTime: 2021-01-06 15:29:27
'''
import sys
sys.path.append("..")

import importlib
import os
import sys
from setuptools import find_packages
from pkgutil import iter_modules


def find_modules(path):
    modules = set()
    for pkg in find_packages(path):
        modules.add(pkg)
        pkgpath = path + '/' + pkg.replace('.', '/')
        if sys.version_info.major == 2 or (sys.version_info.major == 3
                                           and sys.version_info.minor < 6):
            for _, name, ispkg in iter_modules([pkgpath]):
                if not ispkg:
                    modules.add(pkg + '.' + name)
        else:
            for info in iter_modules([pkgpath]):
                if not info.ispkg:
                    modules.add(pkg + '.' + info.name)
    return list(modules)


if __name__ == "__main__":
    module = importlib.__import__('devtool.utils')
    modulePath = os.path.dirname(module.__file__)

    print(find_modules(modulePath))