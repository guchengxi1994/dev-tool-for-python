def k_w(s: str):
    l = s.split(":")
    if len(l) == 2:
        return l[0], l[1]
    else:
        return s, ""


def setDoc(funcName: str):
    while 1 == 1:
        key = input()
        if key != "q!":
            pass
        else:
            break