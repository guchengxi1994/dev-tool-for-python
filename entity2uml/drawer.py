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
# http://www.graphviz.org/doc/info/colors.html
__relations__ = {
    "one2one":{'color':'red'},
    "many2one":{'color':'green'},
    "many2many":{'color':'blue'},
    "one2many":{'color':'gold'}
}

__engines__ = [
    "dot",# 默认布局方式，主要用于有向图
    "neato", # 主要用于无向图
    "twopi" ,# 主要用于径向布局
    "circo" ,# 圆环布局
    "fdp",# 主要用于无向图
    "sfdp" , # 主要绘制较大的无向图
    "patchwork",# 主要用于树哈希图（tree map）
]

from typing import TypeVar


Diagram = TypeVar('Diagram',type,tuple,list)