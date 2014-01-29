GetClosenessCentr
'''''''''''''''''


.. function:: GetClosenessCentr(Graph, NId)

Returns closeness centrality of a given node *NId* in *Graph*. Closeness centrality is equal to 1/farness centrality.

Parameters:

- *Graph*: undirected graph (input)
    A Snap.py undirected graph

- *NId*: int (input)
    Node id

Return value:

- float
    The closeness centrality of the node *NId* in *Graph*

The following example shows how to get the closeness centrality for nodes in 
:class:`TUNGraph`::

    import snap

    vGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    for vNodeIter in vGraph.Nodes():
        print "%d %f" % (vNodeIter.GetId(), \
                         snap.GetClosenessCentr(vGraph, vNodeIter.GetId()))
