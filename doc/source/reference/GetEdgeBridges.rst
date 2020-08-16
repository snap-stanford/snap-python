GetEdgeBridges
''''''''''''''

.. function:: GetEdgeBridges()

A graph method for undirected graphs that returns the edge bridges in a graph. An edge is a bridge if, when removed, increases the number of connected components.

Parameters:

- None

Return value:

- *EdgeV*: :class:`TIntPrV`, a vector of (int, int) pairs
    The bride edges of the graph. Each edge is represented by a node id pair.

The following example shows how to calculate number of bidirectional edges for
:class:`TUNGraph`::

    import snap

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    EdgeV = UGraph.GetEdgeBridges()
    for edge in EdgeV:
        print("edge: (%d, %d)" % (edge.GetVal1(), edge.GetVal2()))
