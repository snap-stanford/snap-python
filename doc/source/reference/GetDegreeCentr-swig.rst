GetDegreeCentr (SWIG)
'''''''''''''''''''''

.. function:: GetDegreeCentr(Graph, NId)

Returns degree centrality of a given node *NId* in *Graph*. Degree centrality of a node is defined as its degree/(N-1), where N is the number of nodes in the network.

Parameters:

- *Graph*: undirected graph (input)
    A Snap.py undirected graph.

- *NId*: int (input)
    A node id in *Graph*.

Return value:

- float
    The degree centrality of the node *NId* in *Graph*.

The following example shows how to get the degree centrality for nodes in :class:`TUNGraph`::

    import snap

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    for NI in UGraph.Nodes():
        DegCentr = snap.GetDegreeCentr(UGraph, NI.GetId())
        print("node: %d centrality: %f" % (NI.GetId(), DegCentr))
