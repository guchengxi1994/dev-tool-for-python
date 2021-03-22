'''
lanhuage: python
Descripttion: 
version: beta
Author: xiaoshuyui
Date: 2021-01-06 08:33:57
LastEditors: xiaoshuyui
LastEditTime: 2021-01-26 15:01:05
'''

import sys
sys.path.append("..")

from devtool import Test, afterExec, beforeExec, infoDecorate, logit, recTime, running, setWrap, testWrapper
from tests.utils import func1
import time


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


@recTime(5)
@logit(save=True, load=False, ignore=False)
def test8(a=1, b=2):

    rs = 'aaaaab'
    # t1 = time.time()
    time.sleep(5)
    # print(time.time() - t1)
    return rs


@beforeExec(beep=True)
@afterExec(beep=True)
def test9(a, b):
    print(a + b)
    time.sleep(1)
    return a + b


@running(gpu=True)
def test10():
    # while 1 == 1:
    #     print(test10.__name__ + ' running')
    #     time.sleep(3)

    i = 0
    while i <= 2:
        print(test10.__name__ + ' running')
        time.sleep(1.5)
        i += 1


@running(mThres=5)
def test11():
    i = 0
    while i <= 2:
        print(test11.__name__ + ' running')
        time.sleep(1.5)
        i += 1


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
    # test6(a=4, b=5)

    # test6(c=4, d=5)

    # test6(a=3, b=4)
    # t1 = time.time()
    # print(test8())

    # print('       '+str(time.time()-t1))

    # test9(1,3)

    test10()
    # test11()
