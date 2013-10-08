GetBfsEffDiam
'''''''''''''

.. function:: GetBfsEffDiam(Graph, NTestNodes, IsDir = false) 

Returns the (approximation of the) Effective Diameter (90-th percentile of the distribution of shortest path lengths) of a graph (by performing BFS from NTestNodes random starting nodes).

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network.

- *NTestNodes*: int (input)
    Number of random nodes from which to start BFS.

- *IsDir*: bool (input)
    false: ignore edge directions and consider edges/paths as undirected (in case they are directed).

Return value:

- *EffDiam*
    The (approximation of the) Effective Diameter of a graph.

The following example shows how to calculate BfsEffDiam for nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    NTestNodes = 10
    IsDir = False
    EffDiam = snap.GetBfsEffDiam(Graph, NTestNodes, IsDir)
    print EffDiam

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    NTestNodes = 10
    IsDir = False
    EffDiam = snap.GetBfsEffDiam(Graph, NTestNodes, IsDir)
    print EffDiam

    Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    NTestNodes = 10
    IsDir = False
    EffDiam = snap.GetBfsEffDiam(Graph, NTestNodes, IsDir)
    print EffDiam
