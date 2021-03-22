import os

import yaml
from prettytable import PrettyTable

reserved_keys = ["definitions", "parameters", "defs", "params", "doc"]


def k_w(s: str):
    l = s.split(":")
    if len(l) == 2:
        return l[0], l[1]
    else:
        return s, ""


def render_table(funcName: str, table: PrettyTable, datas: dict):
    # print(datas)
    if datas:
        thisFunc = datas.get(funcName, None)
        if thisFunc:
            keys = thisFunc.keys()

            if len(list(keys)) > 0:
                for it in list(keys):
                    table.add_row([it, ""])
                    items = thisFunc.get(it, None)
                    table = render_section(table, items)

        print(table) if thisFunc else print()


def render_section(table: PrettyTable, data):
    if type(data) is list:
        for k, v in data[0].items():
            table.add_row([k, render_value(v)])

    elif type(data) is dict:
        for k, v in data.items():
            table.add_row([k, render_value(v)])
    else:
        pass

    return table


def render_value(value):
    if type(value) is str or type(value) is int:
        return value
    elif type(value) is dict:
        t = PrettyTable(["details", ""])
        for k, v in value.items():
            t.add_row([k, render_value(v)])

        # t.border = False
        return t
    elif type(value) is list:
        if value == []:
            return value
        else:
            return ",".join(value)


def setDoc(funcName: str, func=None, path: str = ""):
    if path != "":
        try:
            fs = open(path, encoding="UTF-8")
            datas = yaml.load(fs, Loader=yaml.Loader)
        except:
            raise Exception("File cannot be loaded.")
    else:
        current_path = os.path.abspath(".")
        yaml_path = os.path.join(current_path, "config.yaml")
        fs = open(yaml_path, encoding="UTF-8")
        datas = yaml.load(fs, Loader=yaml.Loader)

    if func:
        co_varnames = func.__code__.co_varnames

        if 'args' in co_varnames:
            co_varnames.remove("args")

        if "kwargs" in co_varnames:
            co_varnames.remove("kwargs")

        table = PrettyTable()

        if len(co_varnames) > 0:
            print("params {} are defined.".format(",".join(co_varnames)))
            render_table(funcName, table, datas)

    saveData = dict()
    obj = dict()
    while 1 == 1:
        key = input()
        if key != "q!":
            k, w = k_w(key)
            if w != "":
                # print(True)
                obj[k] = w
        else:
            saveData[funcName] = obj
            print(saveData)
            break
