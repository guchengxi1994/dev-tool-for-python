'''
lanhuage: python
Descripttion: 
version: beta
Author: xiaoshuyui
Date: 2021-02-20 10:06:56
LastEditors: xiaoshuyui
LastEditTime: 2021-02-20 10:18:45
'''
from difflib import SequenceMatcher


class Test:
    num = 5

    def __init__(self,num1) -> None:
        self.num1 = num1
    
    def p(self):
        print(self.num)


if __name__ == "__main__":
    t = Test(8)
    t.p()
    print(round(SequenceMatcher(None,"abcd","def").ratio(),4))