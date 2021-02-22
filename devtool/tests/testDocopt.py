'''
lanhuage: python
Descripttion: 
version: beta
Author: xiaoshuyui
Date: 2021-02-22 09:04:58
LastEditors: xiaoshuyui
LastEditTime: 2021-02-22 09:24:00
'''

def testFunc1(a, b, c):
    """Usage:
          param a<int>,......
          param b<str>,......
          param c<list>,......

    """
    pass


def testFunc2(*args):
    """Usage:
          param1 <int>,......
          param2 <str>,......
          param3 <list>,......

    """
    print(args)

def testFunc3(**kwargs):
    """Usage:
          param <int>,......
          param <str>,......
          param <list>,......

    """
    print(kwargs)