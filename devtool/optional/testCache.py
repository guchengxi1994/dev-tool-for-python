from functools import lru_cache


@lru_cache()
def test(a=1, b=3):
    print("time to rock!")
    return a + b, a * b, a - b, round(a / b, 2)



if __name__ == "__main__":
    print(test())
    print(test())
    print(test.cache_info())
    print(test(a=3,b=1))