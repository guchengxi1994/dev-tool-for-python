from utils.privilege import BasePrivilege


class BaseRole:
    def __init__(self,name) -> None:
        self.name = name
        self.privilege = None
    
    def auth(self,privilege:BasePrivilege):
        self.privilege = privilege
