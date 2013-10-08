GetEdgeBridges
''''''''''''''
.. note::

    This page is a draft and under revision.


.. function:: GetEdgeBridges(Graph, EdgeV)

    Returns bridge edges of a Graph.

    Edge is a bridge if, when removed, increases the number of connected components. See http://en.wikipedia.org/wiki/Bridge_(graph_theory)

    Parameters:

- *Graph*: undirected graph (input)
    A Snap.py undirected graph.

- *EdgeV*: TIntPrV (output)
    The bride edges of the graph.

    Return value:

    - None


The following example shows how to calculate number of bidirectional edges for
:class:`TNGraph` and :class:`TNEANet`::

    import snap
    Graph = GenRndGnm(PNGraph, 100, 1000)
    EdgeV = TIntPrV()
    GetEdgeBridges(Graph, EdgeV)

    Graph = GenRndGnm(PNEANet, 100, 1000)
    EdgeV = TIntPrV()
    GetEdgeBridges(Graph, EdgeV)



