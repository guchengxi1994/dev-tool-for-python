'''
lanhuage: python
Descripttion: 
version: beta
Author: xiaoshuyui
Date: 2021-01-26 10:54:43
LastEditors: xiaoshuyui
LastEditTime: 2021-01-28 11:16:02
'''
import sys
import inspect


class Te:
    ...


def addSub(c, d):
    t = Te()
    setattr(t, 'name', 'xiaoming')
    print(t.name)
    return c + d


def add(a, b):
    c = 3
    d = 4
    return a + b + addSub(c, d)


class Tracer:
    plot = False
    section = 0

    @classmethod
    def dump(cls, frame, event, arg):
        code = frame.f_code
        module = inspect.getmodule(code)
        module_name = ""
        module_path = ""
        if module:
            module_path = module.__file__
            module_name = module.__name__
        if not cls.plot:
            print(
                event, module_name + '.' + str(code.co_name) + ":" +
                str(frame.f_lineno), frame.f_locals, arg)
            cls.section += 1
            # print(cls.section)
        else:
            pass

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
    t = Tracer()
    t.collect(add, 1, 2)