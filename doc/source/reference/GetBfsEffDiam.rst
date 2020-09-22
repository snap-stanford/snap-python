GetBfsEffDiam
'''''''''''''

.. function:: GetBfsEffDiam(NTestNodes, IsDir=False) 

A graph method that returns the (approximation of the) Effective Diameter (90-th percentile of the distribution of shortest path lengths) of a graph (by performing BFS from NTestNodes random starting nodes).

Parameters:

- *NTestNodes*: int
    The number of random start nodes to use in the BFS used to calculate the graph diameter and effective diameter.

- *IsDir*: bool
    Indicates whether the edges should be considered directed or undirected.

Return value:

- float
    The (approximation of the) Effective Diameter of a graph.

The following example shows how to calculate BfsEffDiam for nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.TNGraph, 100, 1000)
    NTestNodes = 10
    IsDir = False
    EffDiam = Graph.GetBfsEffDiam(NTestNodes, IsDir)
    print(EffDiam)

    UGraph = snap.GenRndGnm(snap.TUNGraph, 100, 1000)
    NTestNodes = 10
    IsDir = False
    EffDiam = UGraph.GetBfsEffDiam(NTestNodes, IsDir)
    print(EffDiam)

    Network = snap.GenRndGnm(snap.TNEANet, 100, 1000)
    NTestNodes = 10
    IsDir = False
    EffDiam = Network.GetBfsEffDiam(NTestNodes, IsDir)
    print(EffDiam)
