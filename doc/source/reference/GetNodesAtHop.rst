GetNodesAtHop
'''''''''''''

.. function:: GetNodesAtHop(StartNId, Hop, IsDir)

A graph method that finds the node ids of all the nodes that are at distance *Hop* from node *StartNId* and stores them in *NIdV*. The function returns the number of nodes found.

Parameters:

- *StartNId*: int
    Starting node id.

- *Hop*: int
    Distance from the starting node.

- *IsDir*: bool
    Indicates whether the edges should be considered directed (True) or undirected (False).

Return value:

- int
    The number of nodes at distance *Hop* from *StartNId*.

- *NIdV*: :class:`TIntV`, a vector of ints 
    Node ids of nodes *Hop* distance away from *StartNId*.


The following example shows how to get a vector of nodes at hop distance
2 away from start node 1 for nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.TNGraph, 100, 1000)
    NodeNum, NodeVec = Graph.GetNodesAtHop(1, 2, True)
    for item in NodeVec:
        print(item)

    UGraph = snap.GenRndGnm(snap.TUNGraph, 100, 1000)
    NodeNum, NodeVec = UGraph.GetNodesAtHop(1, 2, False)
    for item in NodeVec:
        print(item)

    Network = snap.GenRndGnm(snap.TNEANet, 100, 1000)
    NodeNum, NodeVec = Network.GetNodesAtHop(1, 2, True)
    for item in NodeVec:
        print(item)
