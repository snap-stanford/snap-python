GetBfsEffDiam
'''''''''''''

.. function:: GetBfsEffDiam(Graph, NTestNodes, IsDir=False) 

Returns the (approximation of the) Effective Diameter (90-th percentile of the distribution of shortest path lengths) of a graph (by performing BFS from NTestNodes random starting nodes).

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network.

- *NTestNodes*: int (input)
    The number of random start nodes to use in the BFS used to calculate the graph diameter and effective diameter.

- *IsDir*: bool (input)
    Indicates whether the edges should be considered directed or undirected.

Return value:

- float
    The (approximation of the) Effective Diameter of a graph.

The following example shows how to calculate BfsEffDiam for nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    NTestNodes = 10
    IsDir = False
    EffDiam = snap.GetBfsEffDiam(Graph, NTestNodes, IsDir)
    print(EffDiam)

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    NTestNodes = 10
    IsDir = False
    EffDiam = snap.GetBfsEffDiam(UGraph, NTestNodes, IsDir)
    print(EffDiam)

    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    NTestNodes = 10
    IsDir = False
    EffDiam = snap.GetBfsEffDiam(Network, NTestNodes, IsDir)
    print(EffDiam)
