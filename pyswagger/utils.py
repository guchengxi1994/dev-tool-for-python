'''
lanhuage: python
Descripttion: 
version: beta
Author: xiaoshuyui
Date: 2021-02-26 08:46:54
LastEditors: xiaoshuyui
LastEditTime: 2021-02-26 09:29:26
'''
import inspect
import yaml


def getDoc(func):
    return inspect.getdoc(func)


def loadDoc(doc: str):
    assert type(doc) is str and doc != "", "document can not be None or ''"
    yaml_sep = doc.find("---")

    if yaml_sep != -1:
        doc_lines = doc[:yaml_sep - 1]
        swag = yaml.safe_load(doc[yaml_sep:])
    else:
        doc_lines = doc
        swag = None

    return doc_lines, swag
