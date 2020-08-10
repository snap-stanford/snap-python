GetOutDegCnt
''''''''''''

.. function:: GetOutDegCnt()

A graph method that returns the number of nodes for each out-degree as a vector of pairs (out-degree, number of nodes of such out-degree).

Parameters:

- None

Return value:

- *DegToCntV*: :class:`TIntPrV`, a vector of (int, int) pairs
    A vector of (out-degree, number of nodes of such out-degree) pairs.


The following examples shows how to obtain the out-degree histogram for nodes in :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    DegToCntV = Graph.GetOutDegCnt()
    for item in DegToCntV:
        print("%d nodes with out-degree %d" % (item.GetVal2(), item.GetVal1()))

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    DegToCntV = UGraph.GetOutDegCnt()
    for item in DegToCntV:
        print("%d nodes with out-degree %d" % (item.GetVal2(), item.GetVal1()))

    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    DegToCntV = Network.GetOutDegCnt()
    for item in DegToCntV:
        print("%d nodes with out-degree %d" % (item.GetVal2(), item.GetVal1()))
