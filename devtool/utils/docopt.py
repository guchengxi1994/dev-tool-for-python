'''
lanhuage: python
Descripttion: 
version: beta
Author: xiaoshuyui
Date: 2021-02-22 08:45:10
LastEditors: xiaoshuyui
LastEditTime: 2021-02-22 09:36:12
'''
import re
from devtool.utils.devtool_exceptions import DocNotFoundException

reg = 'param <*>'
reg2 = 'param\d? <[a-zA-Z0-9_ ]*>'

def getDoc(func):
    doc = func.__doc__
    if not doc:
        raise DocNotFoundException("Not found docs")

    # o = re.compile(reg)
    print(re.findall(reg2,doc))
