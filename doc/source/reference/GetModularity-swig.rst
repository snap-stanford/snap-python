GetModularity (SWIG)
''''''''''''''''''''

.. function:: GetModularity(Graph, NIdV, GEdges=-1)
   :noindex:

Computes the modularity score of a set of node ids *NIdV* in *Graph*. The function runs much faster if the number of edges in Graph is provided in the optional *GEdges* parameter.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network.

- *NIdV*: :class:`TIntV`, a vector of ints (input)
    The set of nodes ids from which the modularity score will be computed.

- *GEdges*: int (input)
    Optional parameter indicating number of edges in the graph which speeds up the function execution if provided. Note: if GEdges is not equal to the number of edges in the graph, then the computed modularity score will be incorrect.

Return value:

- float
    The modularity score computed from the provided graph and set of node ids. 


The following example shows how to calculate Modularity scores for the first 10 nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Nodes = snap.TIntV()
    for nodeId in range(10):
        Nodes.Add(nodeId)

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    print(snap.GetModularity(Graph, Nodes, 1000))

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    print(snap.GetModularity(UGraph, Nodes, 1000))

    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    print(snap.GetModularity(Network, Nodes, 1000))
