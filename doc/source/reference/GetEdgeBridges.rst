GetEdgeBridges
''''''''''''''

.. function:: GetEdgeBridges(Graph, EdgeV)

    Returns the edge bridges in *Graph* in the vector *EdgeV*. An edge is a bridge if, when removed, increases the number of connected components.

Parameters:

- *Graph*: undirected graph (input)
    A Snap.py undirected graph.

- *EdgeV*: TIntPrV, a vector of (int, int) pairs (output)
    The bride edges of the graph. Each edge is represented by a node id pair.

Return value:

- None

See http://en.wikipedia.org/wiki/Bridge_(graph_theory)

The following example shows how to calculate number of bidirectional edges for
:class:`TNGraph` and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    EdgeV = snap.TIntPrV()
    snap.GetEdgeBridges(Graph, EdgeV)
    for edge in EdgeV:
        print "(%d, %d)" % (edge.GetVal1(), edge.GetVal2())
