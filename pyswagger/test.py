'''
lanhuage: python
Descripttion: 
version: beta
Author: xiaoshuyui
Date: 2021-02-26 08:47:35
LastEditors: xiaoshuyui
LastEditTime: 2021-02-26 09:13:33
'''

from utils import getDoc, loadDoc


def test(a,b,c):
    """Test function of this script.
    ---
    parameters:
       - a : param a
         b : param b
         c : param c
    definitions:
       a :
        type : str
       b :
        type : int
       c :
        type : list

    """
    pass


if __name__ == "__main__":
    document = getDoc(test)
    # d,s = loadDoc(document)

    d,s = loadDoc(test.__doc__)

    print(d)

    print(s)

    # print(document)

    # print("*"*60)

    # print(test.__doc__)