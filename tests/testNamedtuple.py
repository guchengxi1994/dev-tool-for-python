from collections import namedtuple

Friend = namedtuple("Friend", ['name', "age", "sex"])

print(Friend.__doc__)

print(type(Friend))

friend = Friend(name="aaa", age=20, sex="unknow")


def testFunc(_):
    print('wow!')


def testFuncWithParams(_, a, b, c):
    return a + b + c


setattr(Friend, "func1", testFunc)
setattr(Friend, "func2", testFuncWithParams)

print(friend._asdict())
# print(Friend.__dict__)
print(dir(Friend))

# print(friend.func1)
friend.func1()

r = friend.func2(1, 2, 3)
print(r)