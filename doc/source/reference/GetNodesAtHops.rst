GetNodesAtHops
''''''''''''''
.. note::

    This page is a draft and under revision.


.. function:: GetNodesAtHops (Graph, StartNId, HopCntV, IsDir = False)

Returns the number of nodes at each hop distance from the starting node *StartNId*.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

- *StartNId*: int (input)
    Start node id

- *HopCntV*: TIntPrV vector of (int, int) pairs (output)
    Hop count vector

- *IsDir*: boolean (input)
    If False, ignore edge directions and consider edges/paths as undirected (in case they are directed)

Return value:

- int
    Number of different hop distances reachable from *StartNId* (including self-loop)

The following example shows how to obtain number of nodes for each hop distance from randomly selected node *StartNId* in :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    # generate random graph
    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    # initialize vector of pairs
    HopCntV = snap.TIntPrV()
    # get random node id from Graph
    RndNId = Graph.GetRndNId()
    # get number of nodes for each hop distance
    snap.GetNodesAtHops(Graph, RndNId, HopCntV)

    for item in HopCntV:
        print "hops: %d nodes: %d" % (item.Val1(), item.Val2())

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    HopCntV = snap.TIntPrV()
    RndNId = Graph.GetRndNId()
    snap.GetNodesAtHops(Graph, RndNId, HopCntV)

    for item in HopCntV:
        print "hops: %d nodes: %d" % (item.Val1(), item.Val2())

    Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    HopCntV = snap.TIntPrV()
    RndNId = Graph.GetRndNId()
    snap.GetNodesAtHops(Graph, RndNId, HopCntV)

    for item in HopCntV:
        print "hops: %d nodes: %d" % (item.Val1(), item.Val2())
