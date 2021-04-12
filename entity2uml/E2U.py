import importlib
import inspect
import os
import re
import sys
from types import FunctionType, MethodType

from devtool.utils.getModules import get_modules_location
from graphviz import Digraph

from entity2uml import FakeClass, __default_methods__
from entity2uml.drawer import Diagram, __engines__, __formats__, __shapes__

pattern = re.compile("'(.*)'")


class Preparation:
    """ codes should be wrapped in "__main__" function.
    """
    moduleName = ''

    @staticmethod
    def warning():
        print("Warning:" + Preparation.__doc__)

    @classmethod
    def setModuleName(cls, name: str):
        cls.moduleName = name

    @classmethod
    def E2EInspect(cls):
        """Entity to Father-Entity relationshap inpection
        """
        name = ''
        sub_modules = []
        classes = []
        try:
            module = importlib.__import__(cls.moduleName)
            modulePath = os.path.dirname(module.__file__)
            name = module.__name__
            sub_modules = get_modules_location([
                modulePath,
            ], name + ".")
            del module
        except:
            name = __name__

        for i in sub_modules:
            try:
                submodule = importlib.__import__(i)
                res = inspect.getmembers(sys.modules[i], inspect.isclass)
                if res != [] and res is not None:
                    for t in res:
                        classes.append(t[1])
                del submodule
            except Exception:
                pass

        if classes != []:
            for i in classes:
                try:
                    cla = FakeClass.__new__(i)
                    key = pattern.findall(str(i))[0]
                    if key.startswith(cls.moduleName):
                        value = []
                        r = cla.__class__.__bases__
                        for j in r:
                            value.append(pattern.findall(str(j))[0])
                        print(value)

                except:
                    print(
                        "cannot call __new__() on {}, maybe it is an Exception?"
                        .format(str(i)))

    @staticmethod
    def getEntityMap(Entity: type):
        """get a Entity map

        The Entity attributes should be class attributes
        """
        assert type(Entity) is type, "Input type must be 'type'"
        try:
            s = FakeClass.__new__(Entity)
            s_dirs = set(dir(s))
            localAttributes = list(s_dirs.difference(set(__default_methods__)))

            if localAttributes == []:
                print("None attributes found")
                return

            ats = []
            for i in localAttributes:
                a = getattr(Entity, i)
                if type(a) not in [MethodType, FunctionType]:
                    ats.append(i)
            # print(ats)
            return Entity.__name__, ats

        except Exception as e:
            print("Cannot draw :-( .Because {}.".format(e))
            return Entity.__name__, []


class ERMap:
    ermapName = 'drawing.gv'
    ermapComment = "drawing comment"
    savePath = './'
    _format = 'jpg'
    _engine = 'neato'
    _color = 'skyblue'
    dot = Digraph(engine=_engine)

    @classmethod
    def setColor(cls, _color: str):
        assert type(_color) is str, "format must be a not-null string "
        cls._color = _color

    @classmethod
    def setFormat(cls, _format: str):
        assert type(
            _format
        ) is str and _format in __formats__, "format must be a not-null string and in {}".format(
            ",".join(__formats__))
        cls._format = _format

    @classmethod
    def setEngine(cls, _engine: str):
        """set graphviz engine
        """
        assert type(
            _engine
        ) is str and _engine in __engines__, "format must be a not-null string and in {}".format(
            ",".join(__engines__))
        cls._engine = _engine
        cls.dot.engine = cls._engine

    @classmethod
    def setName(cls, name: str):
        assert type(
            name) is str and name != "", "name must be a not-null string"
        cls.ermapName = name

    @classmethod
    def setComment(cls, comment: str):
        assert type(
            comment
        ) is str and comment != "", "comment must be a not-null string"
        cls.ermapComment = comment
        cls.dot.comment = cls.ermapComment

    @classmethod
    def setSavePath(cls, path: str):
        assert type(
            path) is str and path != "", "path must be a not-null string"
        cls.ermapComment = path

    @classmethod
    def _drawEntityMap(cls, Entity: type, index="", render=True):
        name, ats = Preparation.getEntityMap(Entity)
        cls.dot.node("entity" + index, name, shape=__shapes__['entity'])
        # draw attributs
        attrs = []
        for i in range(len(ats)):
            if index == "":
                attrs.append("attr_{}".format(i))
                cls.dot.node("attr_{}".format(i),
                             str(ats[i]),
                             shape=__shapes__['attributes'])
            else:
                attrs.append("attr_{}_{}".format(index, i))
                cls.dot.node("attr_{}_{}".format(index, i),
                             str(ats[i]),
                             shape=__shapes__['attributes'])

        # draw edges
        for i in attrs:
            cls.dot.edge("entity" + index, i, arrowhead="none")

        if render:
            cls.dot.render(cls.savePath + cls.ermapName,
                           view=True,
                           format=cls._format)

    @classmethod
    def drawERDiagram(cls, param: Diagram):
        """tuple : param = (entity1,entity2,"relation","m2n")
           
           m2n should be in __relations__.keys()
        
           List : params = [param1,param2,...,paramN]
        """
        if type(param) is type:
            cls._drawEntityMap(param)

        if type(param) is tuple:
            cls._drawEntityMap(param[0], index="0", render=False)
            cls._drawEntityMap(param[1], index="1", render=False)

            # drawRelation
            cls.dot.node('relation',
                         label=param[2],
                         shape=__shapes__['relation'])

            # drawEdges
            if param[3] == 'one2one':
                label1 = "1"
                label2 = "1"
            if param[3] == 'one2many':
                label1 = "1"
                label2 = "n"
            if param[3] == 'many2one':
                label1 = "n"
                label2 = "1"
            if param[3] == 'many2many':
                label1 = "n"
                label2 = "n"
            cls.dot.edge("entity0", "relation", label=label1, arrowhead="none")
            cls.dot.edge("entity1", "relation", label=label2, arrowhead="none")

            cls.dot.render(cls.savePath + cls.ermapName,
                           view=True,
                           format=cls._format)

        if type(param) is list:
            s = dict()
            ind = 0
            relationInd = 0
            for i in param:
                e1, e2, relation, relationType = i[0], i[1], i[2], i[3]
                if e1.__name__ in s.keys():
                    pass
                else:
                    ind += 1
                    cls._drawEntityMap(e1, index=str(ind), render=False)
                    s[e1.__name__] = str(ind)

                if e2.__name__ in s.keys():
                    pass
                else:
                    ind += 1
                    cls._drawEntityMap(e2, index=str(ind), render=False)
                    s[e2.__name__] = str(ind)

                relationInd += 1
                cls.dot.node('relation' + str(relationInd),
                             label=relation,
                             shape=__shapes__['relation'])

                if relationType == 'one2one':
                    label1 = "1"
                    label2 = "1"
                if relationType == 'one2many':
                    label1 = "1"
                    label2 = "n"
                if relationType == 'many2one':
                    label1 = "n"
                    label2 = "1"
                if relationType == 'many2many':
                    label1 = "n"
                    label2 = "n"

                cls.dot.edge("entity" + s.get(e1.__name__),
                             'relation' + str(relationInd),
                             label=label1,
                             color=cls._color,
                             arrowhead="none")
                cls.dot.edge("entity" + s.get(e2.__name__),
                             'relation' + str(relationInd),
                             label=label2,
                             color=cls._color,
                             arrowhead="none")

            cls.dot.render(cls.savePath + cls.ermapName,
                           view=True,
                           format=cls._format)


class UMLDiagram:
    _engine = 'dot'
    dot = Digraph(engine=_engine)
    ermapName = 'drawing.gv'
    savePath = './'
    _format = 'jpg'

    @classmethod
    def drawUMLDiagram(cls, Entity: type, index="", render=True):
        name, ats = Preparation.getEntityMap(Entity)
        cls.dot.node("entity" + index,
                     "{" + "{}|name1|name2".format(name) + "}",
                     shape="record")

        cls.dot.render(cls.savePath + cls.ermapName,
                       view=True,
                       format=cls._format)
