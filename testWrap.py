'''
lanhuage: python
Descripttion: 
version: beta
Author: xiaoshuyui
Date: 2021-01-06 08:33:57
LastEditors: xiaoshuyui
LastEditTime: 2021-01-08 08:41:31
'''

from devtool.tests.utils import func1

from devtool import logit, testWrapper, setWrap


@setWrap
@testWrapper
def test1():
    print('hello world')


@testWrapper
@setWrap
def test2(aaaa='aaaa'):
    print(aaaa)


@testWrapper
@setWrap
def test3(aaaa='aaaa'):
    assert aaaa is int

@logit
def test4():
    x = 1/0


if __name__ == "__main__":
    # try:
    #     # test3()
    #     test3.__call__()
    # except:
    #     pass

    # print(test3.__annotations__)

    # li = dir(func1)
    # print(li)

    # print(func1.fc1_1.__module__)
    test4()
    print (test4.__annotations__)
