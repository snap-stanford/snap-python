GetFarnessCentr
'''''''''''''''


.. function:: GetFarnessCentr(Graph, NId)

Returns farness centrality of a given node *NId* in *Graph*. Farness centrality of a node is the average shortest path length to all other nodes that reside in the same connected component as the given node.


Parameters:

- *Graph*: undirected graph (input)
    A Snap.py undirected graph

- *NId*: int (input)
    Node id

Return value:

- float:
    The farness centrality of the node *NId* in *Graph*

The following example shows the farness centrality for nodes in 
:class:`TUNGraph`::

    import snap

    vGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    for vNodeIter in vGraph.Nodes():
        print "%d %f" % (vNodeIter.GetId(), \
                         snap.GetFarnessCentr(vGraph, vNodeIter.GetId()))

