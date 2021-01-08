'''
lanhuage: python
Descripttion: 
version: beta
Author: xiaoshuyui
Date: 2021-01-06 08:26:44
LastEditors: xiaoshuyui
LastEditTime: 2021-01-08 10:52:24
'''
import datetime
import importlib
import os

from termcolor import colored

from devtool import __current_platform__, setWrap
from devtool.utils.common import (match_datetime, validate_date,
                                  validate_datetime)
from devtool.utils.getFunctions import find_functions
from devtool.utils.getModules import find_modules
from devtool.utils.logger import logger

BASE_DIR = os.path.abspath(os.curdir)
LOG_PATH = BASE_DIR + os.sep + "DevLog" + os.sep + 'devlog.log'


class DevTool:
    storage = []
    currentModulePath = ''
    currentModuleName = ''

    @classmethod
    def exec(cls, moduleName=''):
        print('<================ Init... ================>')
        module = importlib.__import__(moduleName)
        modulePath = os.path.dirname(module.__file__)
        sub_modules = find_modules(modulePath)
        member_list = find_functions(sub_modules, moduleName)
        for i in member_list:
            try:
                i.func.__call__()
                if i.func.__annotations__.get('wrapped_cached', False):
                    cls.storage.append(i)
            except:
                continue
        print('<================ finish ================>')
        cls.currentModulePath = modulePath
        cls.currentModuleName = moduleName

    @classmethod
    def grep(cls, moduleName: str, grepType, *kwds):
        """
        grepType should be a str in ['and','or'];
        moduleName can be 'this' ,which stands for cls.currentModuleName
        """
        if len(cls.storage) == 0:
            print(
                'Nothing found. Plz run DevTool.go() first or just there is nothing to find.'
            )
        else:
            if grepType not in ['and', 'or']:
                logger.warning(
                    "grepType should be a str in ['and','or'],  but got {}, use 'or' instead."
                    .format(grepType))
                grepType = 'or'

    @classmethod
    def tree(cls, moduleName):
        if cls.currentModulePath == '':
            module = importlib.__import__(moduleName)
            modulePath = os.path.dirname(module.__file__)
        else:
            modulePath = cls.currentModulePath

        for root, _, files in os.walk(modulePath):
            level = root.replace(modulePath, '').count(os.sep)
            dir_indent = "|   " * (level - 1) + "|-- "
            file_indent = "|   " * level + "|-- "
            if not level:
                print('.')
            else:
                tmp = os.path.basename(root)
                if tmp != '__pycache__':
                    print('{}{}'.format(dir_indent, os.path.basename(root)))
                del tmp
            for f in files:
                # tmp = root + os.sep + f
                if not f.endswith('.pyc'):
                    print('{}{}'.format(file_indent, f))

    @staticmethod
    @setWrap
    def logFilter(*kwds, **params):
        """
        kwds are the filters, can be like "ERROR" or function name. Also ,add '-' before kwds means except kwds. eg. '-ERROR' means 'NOT ERROR'
        
        params can be like "from='2021-01-08'","until='2021-01-09'"
        """
        if not os.path.exists(LOG_PATH):
            logger.error('No Log File Found!')
            return
        with open(LOG_PATH, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
            res = []
            # print(len(lines))
            for i in range(0, len(lines)):
                # if validate_datetime(i)
                loggedTime = match_datetime(lines[i])
                for j in kwds:
                    if not j.startswith('-'):
                        if j in lines[i] and loggedTime:
                            res.append([
                                i + 1,
                                datetime.datetime.strptime(
                                    loggedTime[0], '%Y-%m-%d %H:%M:%S')
                            ])
                            break
                    else:
                        if not j in lines[i] and loggedTime:
                            res.append([
                                i + 1,
                                datetime.datetime.strptime(
                                    loggedTime[0], '%Y-%m-%d %H:%M:%S')
                            ])
                            break
            # print(res)
            if len(params) > 0 and len(res) > 0:
                timeFrom = params.get('from', None)
                timeUntil = params.get('until', None)
                if not timeUntil:
                    endTime = datetime.datetime.now()
                else:
                    timeUntil = timeFrom.strip() + ' 23:59:59'
                    endTime = datetime.datetime.strptime(
                        timeUntil, '%Y-%m-%d %H:%M:%S')

                if not timeFrom:
                    startTime = datetime.datetime.strptime(
                        (str(datetime.datetime.now())[:11] + '00:00:00'),
                        '%Y-%m-%d %H:%M:%S')
                else:
                    timeFrom = timeFrom.strip() + ' 00:00:00'
                    startTime = datetime.datetime.strptime(
                        timeFrom, '%Y-%m-%d %H:%M:%S')

                if not startTime < endTime:
                    logger.error(
                        'time from must less than time until but got {},{}'.
                        format(timeFrom, timeUntil))
                    return

                filtRes = []
                for i in res:
                    if i[1] >= startTime and i[1] <= endTime:
                        filtRes.append(i[0])

                print(filtRes)

    @classmethod
    def treeWithState(cls, moduleName):
        if cls.currentModulePath == '':
            module = importlib.__import__(moduleName)
            modulePath = os.path.dirname(module.__file__)
        else:
            modulePath = cls.currentModulePath

        if len(cls.storage) == 0:
            logger.error('Plz run DevTool.go() first.')

        # for i in cls.storage:
        #     print(i.funcName)
        #     print(i.func.__module__)

        for root, dirs, files in os.walk(modulePath):
            level = root.replace(modulePath, '').count(os.sep)
            dir_indent = "|   " * (level - 1) + "|-- "
            file_indent = "|   " * level + "|-- "
            if not level:
                print('.')
            else:
                tmp = os.path.basename(root)
                if tmp != '__pycache__':
                    print('{}{}'.format(dir_indent, os.path.basename(root)))
                del tmp
            for f in files:
                tmp, _ = os.path.splitext(
                    (root + os.sep + f).replace(modulePath,
                                                '').replace(os.sep, '.'))
                if not f.endswith('.pyc'):
                    if len(cls.storage) > 0:
                        for i in cls.storage:
                            tmpModu = i.func.__module__
                            if tmpModu == moduleName + tmp:
                                if __current_platform__ == 'Windows':
                                    text = '{}{}'.format(
                                        file_indent,
                                        f + " --> " + i.funcName + ' --> ' +
                                        str(len(i.func.__annotations__)))
                                else:
                                    text = colored('{}{}'.format(
                                        file_indent,
                                        f + " --> " + i.funcName + ' --> ' +
                                        str(len(i.func.__annotations__))),
                                                   'red',
                                                   attrs=['reverse', 'blink'])
                                print(text)
                            else:
                                print('{}{}'.format(file_indent, f))
                    else:
                        print('{}{}'.format(file_indent, f))
