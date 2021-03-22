'''
lanhuage: python
Descripttion: 
version: beta
Author: xiaoshuyui
Date: 2021-01-06 10:51:46
LastEditors: xiaoshuyui
LastEditTime: 2021-02-20 09:41:13
'''
import sys
sys.path.append("..")

import datetime
import importlib
import inspect

from devtool.devTool import DevTool
# import devtool.tests.utils.func1
from devtool.utils.common import (match_datetime, validate_date,
                                  validate_datetime)

if __name__ == "__main__":
    # name = 'devtool.tests.utils.func1'
    # module = importlib.import_module(name)
    # # print(module)
    # # # print(dir(devtool.tests.utils.func1))
    # member_list = inspect.getmembers(module, predicate=inspect.isfunction)
    # for v,_ in member_list:
    #     print(v)

    DevTool.exec('devtool')

    print(DevTool.storage)

    DevTool.analysis()

    DevTool.grep('this','or','123','True')

    DevTool.treeWithState('devtool')

    # a = match_datetime('2021-01-07 21:19:35,345 - DevTool - ERROR - __main__.test4 Traceback (most recent call last):')
    # b = validate_date('2021-01-07 '.strip())
    # # print(b)
    # print(str(datetime.datetime.now())[:11] + '00:00:00')
    # c = validate_datetime(str(datetime.datetime.now())[:11] + '00:00:00')
    # print(c)
    # DevTool.logFilter('ERROR','INFO',start='122',since='1998-01-01')

    # print(DevTool.logFilter.__annotations__)
