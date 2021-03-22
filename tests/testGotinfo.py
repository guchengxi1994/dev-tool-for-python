'''
lanhuage: python
Descripttion: 
version: beta
Author: xiaoshuyui
Date: 2021-01-25 13:35:00
LastEditors: xiaoshuyui
LastEditTime: 2021-01-25 16:37:18
'''
import sys
sys.path.append("..")

from devtool.utils.common import showPsInfo_after, showPsInfo_before
import time

if __name__ == '__main__':
    ps = showPsInfo_before()
    time.sleep(20)
    showPsInfo_after(ps)

