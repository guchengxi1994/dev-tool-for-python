'''
lanhuage: python
Descripttion: 
version: beta
Author: xiaoshuyui
Date: 2021-01-27 08:33:49
LastEditors: xiaoshuyui
LastEditTime: 2021-01-27 08:38:42
'''
from PIL import Image

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

def get_char(r,g,b,alpha = 256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
 
    unit = (256.0 + 1)/length
    return ascii_char[int(gray/unit)]

if __name__ == '__main__':
    im = Image.open('D:\\testALg\\mask2json\\devTool\\dev-tool-for-python\devtool\\tests\\graph.png')
    im = im.resize((64,64), Image.NEAREST)
 
    txt = ""
 
    for i in range(64):
        for j in range(64):
            txt += get_char(*im.getpixel((j,i)))
        txt += '\n'
 
    print(txt)
