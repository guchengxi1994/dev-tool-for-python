'''
lanhuage: python
Descripttion: 
version: beta
Author: xiaoshuyui
Date: 2021-02-22 09:05:45
LastEditors: xiaoshuyui
LastEditTime: 2021-02-22 09:31:55
'''
import sys
sys.path.append("..")


from devtool.utils.docopt import getDoc
from tests.testDocopt import testFunc1, testFunc2, testFunc3

if __name__ == '__main__':
    # print(testFunc1.__doc__)
    # print(testFunc2.__doc__)
    print(testFunc3.__doc__)

    getDoc(testFunc1)