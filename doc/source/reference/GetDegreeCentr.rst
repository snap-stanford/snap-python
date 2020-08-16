GetDegreeCentr
''''''''''''''

.. function:: GetDegreeCentr(NId)

A graph method for undirected graphs that returns degree centrality of a given node *NId*. Degree centrality of a node is defined as its degree/(N-1), where N is the number of nodes in the graph.

Parameters:

- *NId*: int
    A node id in *Graph*.

Return value:

- float
    The degree centrality of the node *NId*.

The following example shows how to get the degree centrality for nodes in :class:`TUNGraph`::

    import snap

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    for NI in UGraph.Nodes():
        DegCentr = UGraph.GetDegreeCentr(NI.GetId())
        print("node: %d centrality: %f" % (NI.GetId(), DegCentr))
