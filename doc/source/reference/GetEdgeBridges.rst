GetEdgeBridges
''''''''''''''

.. function:: GetEdgeBridges(Graph, EdgeV)

    Returns the edge bridges in *Graph* in the vector *EdgeV*. An edge is a bridge if, when removed, increases the number of connected components.

Parameters:

- *Graph*: undirected graph (input)
    A Snap.py undirected graph.

- *EdgeV*: :class:`TIntPrV`, a vector of (int, int) pairs (output)
    The bride edges of the graph. Each edge is represented by a node id pair.

Return value:

- None


The following example shows how to calculate number of bidirectional edges for
:class:`TNGraph` and :class:`TNEANet`::

    import snap

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    EdgeV = snap.TIntPrV()
    snap.GetEdgeBridges(UGraph, EdgeV)
    for edge in EdgeV:
        print "edge: (%d, %d)" % (edge.GetVal1(), edge.GetVal2())
