from tests.testEntities.Base import Eighth, Seventh, Sixth
from entity2uml import E2U
from devtool.devTool import DevTool
import inspect


class A:
    def __init__(self, a: str, b: int) -> None:
        self.a = a
        self.b = b


class B(A):
    def __init__(self, a: str = "", b: int = 0) -> None:
        self.a = a
        self.b = b


class C(B):
    ...


if __name__ == "__main__":
    print("===================")
    E2U.Preparation.warning()
    E2U.Preparation.setModuleName("tests.testEntities")
    E2U.Preparation.E2EInspect()
    print("===================")

    # s = Sixth("a","b")
    # print(dir(s))

    # s2 = C.__new__(Sixth)
    # print(type(Sixth) is type)
    # print(dir(s2))

    # print(inspect.ismethod(s2.testMethod))

    # func = getattr(s2,"testMethod")
    # print(type(func))

    # print("X"*20)

    # E2U.Preparation.getEntityMap(Sixth)

    # E2U.ERMap.drawEntityMap(Sixth)

    params = [(Sixth, Seventh, 'has', "one2one"),
              (Seventh, Eighth, 'has', "one2one"),
              (Sixth, Eighth, 'has', "one2one")]

    # E2U.ERMap.drawERDiagram((Sixth, Seventh, 'has', "one2one"))
    E2U.ERMap.setColor('yellow')
    E2U.ERMap.setComment('balabombka')
    E2U.ERMap.drawERDiagram(params)
