'''
lanhuage: python
Descripttion: 
version: beta
Author: xiaoshuyui
Date: 2021-01-06 08:33:57
LastEditors: xiaoshuyui
LastEditTime: 2021-01-06 10:46:24
'''

from devtool.tests.utils import func1

from devtool import testWrapper, isWrapped


@isWrapped
@testWrapper
def test1():
    print('hello world')


@testWrapper
@isWrapped
def test2(aaaa='aaaa'):
    print(aaaa)


@testWrapper
@isWrapped
def test3(aaaa='aaaa'):
    assert aaaa is int


if __name__ == "__main__":
    # try:
    #     # test3()
    #     test3.__call__()
    # except:
    #     pass

    # print(test3.__annotations__)

    li = dir(func1)
    print(li)

    print(func1.fc1_1.__module__)
