'''
lanhuage: python
Descripttion: 
version: beta
Author: xiaoshuyui
Date: 2021-01-06 08:26:44
LastEditors: xiaoshuyui
LastEditTime: 2021-01-06 11:38:24
'''
import importlib
import inspect
import os

class DevTool:
    @classmethod
    def do(self,moduleName=''):
        print('<================ Init... ================>')
        try:
            module = importlib.__import__(moduleName)
            print(os.path.dirname(module.__file__))
            # member_list = inspect.getmembers(module, predicate=inspect.isfunction)

            member_list = inspect.getmembers(module, predicate=inspect.ismodule)

            for func_name, func in member_list:
                print(func_name)
                print(func)

        except Exception as e:
            print(e)
        print('<================ finish ================>')