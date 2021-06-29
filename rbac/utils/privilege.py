from utils.do import Do


class BasePrivilege(object):
    def __init__(self, name) -> None:
        super().__init__()
        self.name = name
        self.privilege = []
    
    def add(self,do:Do):
        self.privilege.append(do)