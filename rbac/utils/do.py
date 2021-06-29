import abc
from typing import Any
from utils.exception import FileCannotAccessException


class Do:
    @abc.abstractmethod
    def howTo(self, T: Any):
        pass


class Do_On_File_Base(Do):
    def howTo(self, filename):
        import os
        if not os.path.exists(filename):
            raise FileCannotAccessException(
                "can not found file {}".format(filename))
        del os
    
    def _read(self):pass