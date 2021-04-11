class Base:...
 
class Second(Base):...

class Third(Second,Base):...

class Fourth(Third):...

class Fifth(Base):...

class Sixth(Fifth):
    clsParam = 'aaa'
    clsParam2 = 'bbb'
    def __init__(self,name:str,sex:str) -> None:
        self.name = name
        self.sex = sex
    
    def testMethod(self):...

class Seventh(Fifth):
    clsParam3 = 'ccc'
    clsParam4 = 'ddd'
    def __init__(self,name:str='',sex:str='') -> None:
        self.name = name
        self.sex = sex