<!--
 * @lanhuage: markdown
 * @Descripttion: 
 * @version: beta
 * @Author: xiaoshuyui
 * @Date: 2021-01-06 08:24:38
 * @LastEditors: xiaoshuyui
 * @LastEditTime: 2021-01-08 11:04:10
-->
# dev-tool-for-python
 a small tool for python development

[![Build Status](https://www.travis-ci.com/guchengxi1994/dev-tool-for-python.svg?branch=dev)](https://www.travis-ci.com/guchengxi1994/dev-tool-for-python.svg?branch=dev)


# Introduction

### Recently, I have wrote a lot of python codes but always like this.

![devtool-example](./static/devtool_example.gif)

![wtf](./static/wtf.jpg)

#### I think i am a bad programmer. o(￣ヘ￣o＃)

#### I will forget where can i find the proper function or method even with a doc-string.(But i seldom write doc-string when coding alone.)

## So i want to develop a tool to record informations when coding by using python decorators.

# HOW TO USE.

## 1. Download this repo. run

    pip install -r requestments.txt

## 2. Copy the "devtool" folder into your project.

## 3. Details.

### 3.1 For logs filter.

    from devTool import DevTool
    DevTool.logFilter(*kwds, **params)

kws are the keywords to be searched,params include path,since and until under this version.

To record log file easily,try this.

    from devTool import logit

    @logit
    def test4():
        x = 1 / 0
    
    test4()

then DevLog/devlog.log will be created and log information will be added.

    2021-01-09 09:49:00,143 - DevTool - ERROR - __main__.test4 Traceback (most recent call last):
    File "D:\dev-tool-for-python\devtool\__init__.py", line 112, in execute
        func(*args, **kwargs)
    File ".\testWrap.py", line 35, in test4
        x = 1 / 0
    ZeroDivisionError: division by zero


![linux](./static/devtool_linux.gif)

