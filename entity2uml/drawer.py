"""
shapes can be found here： http://www.graphviz.org/doc/info/shapes.html
"""

__shapes__ = {
    'entity':"rectangle",
    'relation':"diamond",
    'attributes':'ellipse'
}

__formats__ = [ 
    "jpg",
    "bmp",
    "png"
]

# map <str,style>  style is graphviz line style
__relations__ = {
    "one2one":"",
    "many2one":"",
    "many2many":"",
    "one2many":""
}

from typing import TypeVar


Diagram = TypeVar('Diagram',type,tuple,list)