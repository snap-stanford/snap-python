GetModularity
'''''''''''''

.. function:: GetModularity(NIdV, GEdges=-1)

A graph method that computes the modularity score of a set of node ids *NIdV*. The function runs much faster if the number of edges is provided in the optional *GEdges* parameter.

Parameters:

- *NIdV*: Python list or :class:`TIntV`, a vector of ints
    The set of nodes ids from which the modularity score will be computed.

- (optional) *GEdges*: int
    A parameter providing the number of edges in the graph which speeds up the function execution if provided. Note: if GEdges must be equal to the number of edges in the graph, otherwise the computed modularity score will be incorrect.

Return value:

- float
    The modularity score computed from the provided graph and set of node ids. 


The following example shows how to calculate Modularity scores for the first 10 nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Nodes = []
    for nodeId in range(10):
        Nodes.append(nodeId)

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    print(Graph.GetModularity(Nodes, 1000))

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    print(UGraph.GetModularity(Nodes, 1000))

    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    print(Network.GetModularity(Nodes, 1000))
