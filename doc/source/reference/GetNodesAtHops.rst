GetNodesAtHops
''''''''''''''

.. function:: GetNodesAtHops (Graph, StartNId, HopCntV, IsDir = False)

Fills *HopCntV* with pairs (hop distance from *StartNId*, number of nodes at that hop distance). The function returns the number of different hop distances reachable from *StartNId*.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network.

- *StartNId*: int (input)
    Starting node id.

- *HopCntV*: TIntPrV, a vector of (int, int) pairs (output)
    Vector of (hop distance, number of nodes at that distance) pairs.

- *IsDir*: bool (input)
    Indicates whether the edges should be considered directed or undirected.

Return value:

- int
    Number of different hop distances reachable from *StartNId*, including self-loops.


The following example shows how to obtain number of nodes for each hop distance from node 1 in :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    NodeVec = snap.TIntPrV()
    snap.GetNodesAtHops(Graph, 1, NodeVec, True)
    for item in NodeVec:
        print "%d, %d" % (item.GetVal1(), item.GetVal2())

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    NodeVec = snap.TIntPrV()
    snap.GetNodesAtHops(UGraph, 1, NodeVec, True)
    for item in NodeVec:
        print "%d, %d" % (item.GetVal1(), item.GetVal2())

    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    NodeVec = snap.TIntPrV()
    snap.GetNodesAtHops(Network, 1, NodeVec, True)
    for item in NodeVec:
        print "%d, %d" % (item.GetVal1(), item.GetVal2())
