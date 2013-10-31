GetDegreeCentr
''''''''''''''


.. function:: GetDegreeCentr(Graph, NId)

Returns Degree centrality of a given node *NId* in *Graph*. Degree centrality of a node is defined as its degree/(N-1), where N is the number of nodes in the network.

Parameters:

- *Graph*: undirected graph (input)
    A Snap.py undirected graph

- *NId*: int (input)
    Node id

Return value:

- float
    The degree centrality of the node *NId* in *Graph*

The following example shows how to get the degree Centrality for nodes in :class:`TUNGraph`::

    import snap

    vGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    for vNodeIter in vGraph.Nodes():
        print "%d %f" % (vNodeIter.GetId(), \
                         snap.GetDegreeCentr(vGraph, vNodeIter.GetId()))
