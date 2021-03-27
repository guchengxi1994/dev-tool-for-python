from collections import OrderedDict
from typing import Any
import time


class LRU(OrderedDict):
    defaultSize = 100
    cache = OrderedDict()

    @classmethod
    def _set(cls, key, value):
        if key in cls.cache:
            del cls.cache[key]
            cls.cache[key] = value
        else:
            if len(cls.cache) == cls.defaultSize:
                cls.cache.popitem(last=False)
            cls.cache[key] = value

    @classmethod
    def _get(cls, key):
        if key in cls.cache:
            val = cls.cache[key]
            del cls.cache[key]
            cls.cache[key] = val
            return val
        else:
            return None


class LRUDecorator(LRU):
    def __init__(self, func):
        super().__init__()
        self.func = func

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        val = super()._get(self.func.__name__)
        if val is None:
            res = self.func(*args, **kwds)
            super()._set(self.func.__name__, res)
            return res
        else:
            val = super()._get(self.func.__name__)
            return val


@LRUDecorator
def test(a=1, b=2):
    time.sleep(5)
    return a + b


@LRUDecorator
def test2(a=1, b=2):
    return a - b


if __name__ == "__main__":
    t1 = time.time()
    test()
    print(LRUDecorator.cache)

    t2 = time.time()
    print(t2 - t1)

    test()
    print(LRUDecorator.cache)

    t3 = time.time()
    print(t3 - t2)

    test2()
    print(LRUDecorator.cache)
