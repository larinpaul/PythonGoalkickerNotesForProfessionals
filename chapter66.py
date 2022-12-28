# ### 2022 12 18 ### 14:57 ###

# #### Chapter 66: graph-tool

# # The python tools can be used to generate graph

# ## Section 66.1: PyDotPlus

# # PyDotPlus is an improved version of the old pydot project that provides a Pythno Interface to Graphviz's Dot
# # langauge.

# # Installation

# # For the latest stable version:
# pip install pydotplus

# # For the developmentversion:
# pip install https://github.com/carlos-jenkins/pydotplus/archive/master.zip

# # Load graphs as defined by a DOT file

# # The file is assumed to be in DOT format. It will be loaded, parsed and a DOt class will be returned,
# # representing the graph. For example, a simple demo.do:
# digraph demo1{a->b->c;c->a;}
# import pydotplus
# graph_a = pydotplus.graph_from_dot_file('demo.dot')
# graph_a.write_svg('test.svg') # generate grapg in svg.

# # You willget a svg(Scalable Vector Graphics) like this:

# ### ... ###


# ## Section 66.2: PyGraphviz

# # Get PyGraphviz from the Python Package Index at http//pypi.python.org/pypi/pygraphviz

# # or install it with:
# # pip install pygraphviz

# #  and an attempt will be made to find and install an appropriate version that matches your operating system and
# # python version.

# # You can install the development version (at github.com) with:
# # pip install git://githib.com/pygraphviz/pygraphviz.git#egg=pygaphviz

# # Get PyGraphviz from the Python Package Index at http://pypi.pytho.org/pypi/pygraphviz

# # or install it with:
# # easy_install pygraphviz

# # an an attempt will be made tofind and install an appropriate version that matches your operating system adn
# # Python verson.

# # Load graph as defined by a DOT file

# # The file is assumed to be in DOT format. It will be laoded, parsed and a Dot classs will be returned,
# # representing the graph. For example, a simple demo.dot:
# # digraph demo1{a->b->c;c->a;}

# # Lod it and draw it.
# import pygraphviz as pgv
# G = pgv.AGraph("demo.dot")
# G.draw('test', format='svg', prog='dot')

# # You will get a svg(Scalable Vector Graphics)
