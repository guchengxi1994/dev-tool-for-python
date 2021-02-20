'''
lanhuage: python
Descripttion: 
version: beta
Author: xiaoshuyui
Date: 2021-01-28 08:47:04
LastEditors: xiaoshuyui
LastEditTime: 2021-02-20 10:41:28
'''

import inspect
import sys
from devtool.utils.common import plotBeautify
from devtool.utils import __start__, __block__, __arrow__, __end__, do_nothing


class GraphTracer:
    plot = False
    section = 0

    @classmethod
    def setPlot(cls, plot):
        cls.plot = plot

    @classmethod
    def dump(cls, frame, event, arg):
        code = frame.f_code
        module = inspect.getmodule(code)
        module_name = ""
        if module:
            module_name = module.__name__

        if not cls.plot:
            print(
                event, module_name + '.' + str(code.co_name) + ":" +
                str(frame.f_lineno), frame.f_locals, arg)
        else:
            cls.section += 1
            p1 = plotBeautify(str(event))
            p2 = plotBeautify(str(module_name))
            p3 = plotBeautify(
                str(str(code.co_name) + ":" + str(frame.f_lineno)))
            p4 = plotBeautify(str(arg))
            print(__start__) if str(event) == 'call' else do_nothing()
            print(__block__.format(cls.section, p1, p2, p3, p4))
            print(__arrow__) if str(event) != 'return' else print(__end__)

    @classmethod
    def trace(cls, frame, event, arg):
        cls.dump(frame, event, arg)
        return cls.trace

    @classmethod
    def collect(cls, func, *args, **kwargs):
        sys.settrace(cls.trace)
        func(*args, **kwargs)
        sys.settrace(None)


if __name__ == "__main__":
    from devtool.tests.testSystrace import add
    t = GraphTracer()
    t.collect(add, 1, 2)