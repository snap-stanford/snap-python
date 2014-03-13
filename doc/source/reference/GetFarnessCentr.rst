GetFarnessCentr
'''''''''''''''

.. function:: GetFarnessCentr(Graph, NId)

Returns farness centrality of a given node *NId* in *Graph*. Farness centrality of a node is the average shortest path length to all other nodes that reside in the same connected component as the given node.

Parameters:

- *Graph*: undirected graph (input)
    A Snap.py undirected graph.

- *NId*: int (input)
    A node id in *Graph*.

Return value:

- float
    The farness centrality of the node *NId* in *Graph*.


The following example shows how to get the farness centrality for nodes in 
:class:`TUNGraph`::

    import snap

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    for NI in UGraph.Nodes():
        FarCentr = snap.GetFarnessCentr(UGraph, NI.GetId())
        print "node: %d centrality: %f" % (NI.GetId(), FarCentr)

