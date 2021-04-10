'''
lanhuage: python
Descripttion: 
version: beta
Author: xiaoshuyui
Date: 2021-01-26 12:16:59
LastEditors: xiaoshuyui
LastEditTime: 2021-01-26 14:40:24
'''
import sys
sys.path.append("..")

from devtool.utils.common import plotBeautify
from devtool.utils import __block__,__arrow__
from devtool import Tracer, traceplot

# print(__block__.format(0,1,2,3,4))

# p1 = int(22/2 - 0.5*len(str(1)))*' ' + str(1) + int(22/2 - 0.5*len(str(1)))*' '
# p2 = int(22/2 - 0.5*len(str(2)))*' ' + str(2) + int(22/2 - 0.5*len(str(2)))*' '
# p3 = int(22/2 - 0.5*len(str(3)))*' ' + str(3) + int(22/2 - 0.5*len(str(3)))*' '
# p4 = int(22/2 - 0.5*len(str(4)))*' ' + str(4) + int(22/2 - 0.5*len(str(4)))*' '

# print(__arrow__)

# print(__block__.format(0,p1,p2,p3,p4))

# p5 = plotBeautify(str(5))
# p6 = plotBeautify(str(6))
# p7 = plotBeautify(str(7))
# p8 = plotBeautify(str(8))


# print(__arrow__)

# print(__block__.format(0,p5,p6,p7,p8))

@traceplot(False)
def add1(a, b):
    c = 3
    d = 4
    e = c + d
    return a + b + e

@traceplot()
def add2(a, b):
    c = 3
    d = 4
    e = c + d
    return a + b + e

if __name__ == "__main__":
    # t = Tracer()
    # t.collect(add, 1, 2)
    add1(3,4)
    add2(3,4)
