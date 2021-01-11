'''
lanhuage: python
Descripttion: 
version: beta
Author: xiaoshuyui
Date: 2021-01-06 08:33:57
LastEditors: xiaoshuyui
LastEditTime: 2021-01-11 19:27:59
'''

from devtool import Test, infoDecorate, logit, recTime, setWrap, testWrapper
from devtool.tests.utils import func1


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


@logit()
def test4():
    x = 1 / 0


@infoDecorate('a test', id='bb', name='cc')
def test5():
    print('aaaaaaaaaaaaaa')


@Test(a=43, b=12)
def test6(a, b):
    print(a + b)


@logit()
def test7(a, b):
    print(a + b)
    return a + b

@recTime
@logit(save=True,load=True,ignore=False)
def test8(a=1,b=2):
    import time
    rs = 'aaaaab'
    t1 = time.time()
    time.sleep(5)
    print(time.time()-t1)
    return rs


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
    # print(test4())
    # print (test4.__annotations__)

    # test5()
    # print(test5.__annotations__)

    # test6()

    # a = test7(1,3)
    # print(a)

    # a = test8(a=3,b=4)
    # print(a)
    test6(a=4, b=5)

