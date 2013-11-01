GetNodesAtHop
'''''''''''''

.. function:: GetNodesAtHop(Graph, StartNId, Hop, NIdV, IsDir)

Finds the node ids of all the nodes that are at distance *Hop* from node *StartNId* and stores them in *NIdV*. The function returns the number of nodes found.

Parameters:

- *PGraph*: graph (input)
    A Snap.py graph or a network

- *StartNId*: int (input)
    Starting node id

- *Hop*: int (input)
    Distance from the starting node

- *NIdV*: TIntV, a vector of ints (output)
    Node ids of nodes *Hop* distance away from *StartNId*.

- *IsDir*: bool (input)
    Boolean specifying whether the graph is directed. If false, edge directions are ignored and considered as undirected.

Return value:

- int
    The number of nodes at distance *Hop* from *StartNId*

The following example shows how to get a vector of nodes at hop distance
2 away from start node 1 for nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    NodeVec = snap.TIntV()
    snap.GetNodesAtHop(Graph, 1, 2, NodeVec, True)
    for item in NodeVec:
        print item

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    NodeVec = snap.TIntV()
    snap.GetNodesAtHop(Graph, 1, 2, NodeVec, True)
    for item in NodeVec:
        print item

    Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    NodeVec = snap.TIntV()
    snap.GetNodesAtHop(Graph, 1, 2, NodeVec, True)
    for item in NodeVec:
        print item
