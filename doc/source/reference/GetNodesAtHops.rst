GetNodesAtHops
''''''''''''''

.. function:: GetNodesAtHops (StartNId, IsDir=False)

A graph method that computes the number of nodes at different hop distances reachable from *StartNId*. It returns the number of different hops and pairs (hop distance from *StartNId*, number of nodes at that hop distance).

Parameters:

- *StartNId*: int
    Starting node id.

- *IsDir*: bool
    Indicates whether the edges should be considered directed (True) or undirected (False).

Return value:

- int
    Number of different hop distances reachable from *StartNId*, including self-loops.

- *HopCntV*: :class:`TIntPrV`, a vector of (int, int) pairs
    Vector of (hop distance, number of nodes at that distance) pairs.


The following example shows how to obtain number of nodes for each hop distance from node 1 in :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.TNGraph, 100, 1000)
    NodeNum, NodeVec = Graph.GetNodesAtHops(1, True)
    for item in NodeVec:
        print("%d, %d" % (item.GetVal1(), item.GetVal2()))

    UGraph = snap.GenRndGnm(snap.TUNGraph, 100, 1000)
    NodeNum, NodeVec = UGraph.GetNodesAtHops(1, False)
    for item in NodeVec:
        print("%d, %d" % (item.GetVal1(), item.GetVal2()))

    Network = snap.GenRndGnm(snap.TNEANet, 100, 1000)
    NodeNum, NodeVec = Network.GetNodesAtHops(1, True)
    for item in NodeVec:
        print("%d, %d" % (item.GetVal1(), item.GetVal2()))
