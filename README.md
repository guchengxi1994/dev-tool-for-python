<!--
 * @lanhuage: markdown
 * @Descripttion: 
 * @version: beta
 * @Author: xiaoshuyui
 * @Date: 2021-01-06 08:24:38
 * @LastEditors: xiaoshuyui
 * @LastEditTime: 2021-01-15 14:12:34
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

    from devtool.devTool import DevTool
    DevTool.logFilter(*kwds, **params)

kws are the keywords to be searched,params include path,since and until under this version.

To record log file easily,try this.

    from devtool import logit

    @logit()
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

@logit can add three params: save,load,ignore

@save ,to record the function ,params and result to DevLog/devCache.dump

@load, load result from DevLog/devCache.dump if the function costs much time. if the params are same to the stored params, then return the result. Otherwise, excute again.

@ignore, force to execute the function 

    @logit(save=True,load=True,ignore=False)
    def test8(a=1,b=2):
        import time
        rs = 'aaaaab'
        t1 = time.time()
        time.sleep(5)
        print(time.time()-t1)
        return rs

    if __name__ == "__main__":
        a = test8(a=3,b=4)
        print(a)


first time:

    (base) PS D:\dev-tool-for-python> python .\testWrap.py
    5.01481556892395
    aaaaab

second time:

    (base) PS D:\dev-tool-for-python> python .\testWrap.py
    aaaaab


![linux](./static/devtool_linux.gif)

### 3.2 init a new python project

    from devtool.devTool import DevTool

    if __name__ == "__main__":
        DevTool.initProject('Test')

![initproject](./static/devtool_init_project.gif)

If 'DevTool.initProject' got a param 'tree=True', then

    This script needs a parameter "path",but got "",using D:\testALg\mask2json\devTool\dev-tool-for-python\Test instead.
    Init finishes.
    .
    |-- main.py
    |-- static
    |-- tests
    |-- utils
    |   |-- __init__.py

The structure of project is stored in [style.yaml](./devtool/style.yaml).

    MINE:
        scripts:
            main : root/main.py
            utils_init : root/utils/__init__.py
        folders:
            static : root/static
            utils : root/utils
            tests : root/tests

And "MINE" is my style. :)

