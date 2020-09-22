GetInDegCnt
'''''''''''

.. function:: GetInDegCnt(Graph, DegToCntV)

A graph method that returns the number of nodes for each in-degree as a vector of pairs (in-degree, number of nodes of such in-degree).

Parameters:

- None

Return value:

- *DegToCntV*: :class:`TIntPrV`, a vector of (int, int) pairs
    A vector of (in-degree, number of nodes of such in-degree) pairs.


The following examples shows how to obtain the in-degree histogram for nodes in :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.TNGraph, 100, 1000)
    DegToCntV = Graph.GetInDegCnt()
    for item in DegToCntV:
        print("%d nodes with in-degree %d" % (item.GetVal2(), item.GetVal1()))

    UGraph = snap.GenRndGnm(snap.TUNGraph, 100, 1000)
    DegToCntV = UGraph.GetInDegCnt()
    for item in DegToCntV:
        print("%d nodes with in-degree %d" % (item.GetVal2(), item.GetVal1()))

    Network = snap.GenRndGnm(snap.TNEANet, 100, 1000)
    DegToCntV = Network.GetInDegCnt()
    for item in DegToCntV:
        print("%d nodes with in-degree %d" % (item.GetVal2(), item.GetVal1()))
