def block(_blockType: str = "strong"):
    def decorate(func):
        def inner(*args, **kwargs):
            if _blockType != "strong":
                return func(*args, **kwargs)
            else:
                return None

        return inner

    return decorate


@block()
def test(a=1, b=2):
    print(a + b)


if __name__ == "__main__":
    test()
