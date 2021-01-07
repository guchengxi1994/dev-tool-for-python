'''
lanhuage: python
Descripttion: 
version: beta
Author: xiaoshuyui
Date: 2021-01-06 10:51:46
LastEditors: xiaoshuyui
LastEditTime: 2021-01-07 08:48:35
'''
# import devtool.tests.utils.func1
import importlib
from devtool.devTool import DevTool
import inspect

if __name__ == "__main__":
    # name = 'devtool.tests.utils.func1'
    # module = importlib.import_module(name)
    # # print(module)
    # # # print(dir(devtool.tests.utils.func1))
    # member_list = inspect.getmembers(module, predicate=inspect.isfunction)
    # for v,_ in member_list:
    #     print(v)

    DevTool.exec('devtool')

    DevTool.treeWithState('devtool')
