'''
lanhuage: python
Descripttion: 
version: beta
Author: xiaoshuyui
Date: 2021-01-06 15:13:32
LastEditors: xiaoshuyui
LastEditTime: 2021-01-06 16:26:01
'''
import sys
from setuptools import find_packages
from pkgutil import iter_modules, walk_packages


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


def get_modules_location(path, name):
    res = set()
    for _, modname, _ in walk_packages(path,
                                       prefix=name,
                                       onerror=lambda x: None):
        res.add(modname)

    return list(res)