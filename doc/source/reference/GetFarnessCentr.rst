GetFarnessCentr
'''''''''''''''

.. function:: GetFarnessCentr(Graph, NId)

Returns Farness centrality of a given node *NId* in *Graph*. Farness centrality of a node is the average shortest path length to all other nodes that reside in the same connected component as the given node.

Parameters:

- *Graph*: graph (input)
    A Snap.py undirected graph

- *NId*: int (input)
    Node ID

Return value:

- double

The following example shows the Farness centrality for nodes in 
:class:`TUNGraph`::

    import snap

    vGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    for vNodeIter in vGraph.Nodes():
        print '%d %f' % (vNodeIter.GetId(), \
                         snap.GetFarnessCentr(vGraph, vNodeIter.GetId()))

