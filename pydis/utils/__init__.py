import platform

__end_mark__ = "\n"

if platform.system().lower == "windows":
    __end_mark__ = "\r\n"

del platform