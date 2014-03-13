GetClosenessCentr
'''''''''''''''''

.. function:: GetClosenessCentr(Graph, NId)

Returns closeness centrality of a given node *NId* in *Graph*. Closeness centrality is equal to 1/farness centrality.

Parameters:

- *Graph*: undirected graph (input)
    A Snap.py undirected graph.

- *NId*: int (input)
    A node id in *Graph*.

Return value:

- float
    The closeness centrality of the node *NId* in *Graph*.


The following example shows how to get the closeness centrality for nodes in 
:class:`TUNGraph`::

    import snap

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    for NI in UGraph.Nodes():
        CloseCentr = snap.GetClosenessCentr(UGraph, NI.GetId())
        print "node: %d centrality: %f" % (NI.GetId(), CloseCentr)
