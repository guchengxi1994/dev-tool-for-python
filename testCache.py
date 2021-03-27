# from functools import lru_cache
from devtool.optional.cache import LRUDecorator


@LRUDecorator
def test1(a=1, b=3):
    print("time to rock!")
    return a + b, a * b, a - b, round(a / b, 2)

@LRUDecorator
def test2(a=1, b=3):
    print("time to rock!")
    return a + b, a * b, a - b, round(a / b, 2)



if __name__ == "__main__":
    print(test1())
    print("*"*60)
    print(test1())
    print("*"*60)
    # print(test.cache_info())
    print(test2(a=3,b=1))