GetDegCnt
'''''''''''''''

.. function:: GetDegCnt()

A graph method that returns the number of nodes for each degree as a vector of pairs (degree, number of nodes of such degree).

Parameters:

- None

Return value:

- *DegToCntV*: :class:`TIntPrV`, a vector of (int, int) pairs
    A vector of (degree, number of nodes of such degree) pairs.

The following examples shows how to obtain the degree histogram for nodes in :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.TNGraph, 100, 1000)
    DegToCntV = Graph.GetDegCnt()
    for item in DegToCntV:
        print("%d nodes with degree %d" % (item.GetVal2(), item.GetVal1()))

    UGraph = snap.GenRndGnm(snap.TUNGraph, 100, 1000)
    DegToCntV = UGraph.GetDegCnt()
    for item in DegToCntV:
        print("%d nodes with degree %d" % (item.GetVal2(), item.GetVal1()))

    Network = snap.GenRndGnm(snap.TNEANet, 100, 1000)
    DegToCntV = Network.GetDegCnt()
    for item in DegToCntV:
        print("%d nodes with degree %d" % (item.GetVal2(), item.GetVal1()))
