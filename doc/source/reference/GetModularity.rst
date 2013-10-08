GetModularity
'''''''''''''

.. function:: GetModularity(Graph, NIdV, GEdges=-1)

Computes the Modularity score of a set of node ids NIdV in *Graph*. The function runs much faster if the number of edges in Graph is provided in the optional GEdges parameter.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

- *NIdV*: TIntV vector of node ids (input)
    The set of nodes ids from which the modularity score will be computed.

- *GEdges*: int (input)
    Optional parameter indicating number of edges in the graph which speeds up the function execution if provided. Note: if GEdges is not equal to the number of edges in the graph, then the computed modularity score will be incorrect.

Return value:

- *Modularity* float (output)
    The modularity score computed from the provided graph and set of node ids. 

For more info see: http://en.wikipedia.org/wiki/Modularity_%28networks%29

The following example shows how to calculate Modularity scores for the first 10 nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    Nodes = snap.TIntV()
    for nodeId in range(1,10):
        Nodes.Add(nodeId)
    print snap.GetModularity(Graph, Nodes, 1000)

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    Nodes = snap.TIntV()
    for nodeId in range(1,10):
        Nodes.Add(nodeId)
    print snap.GetModularity(Graph, Nodes, 1000)

    Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    Nodes = snap.TIntV()
    for nodeId in range(1,10):
        Nodes.Add(nodeId)
    print snap.GetModularity(Graph, Nodes, 1000)

