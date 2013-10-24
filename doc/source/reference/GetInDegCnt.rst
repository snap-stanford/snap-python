GetInDegCnt
'''''''''''


.. function:: GetInDegCnt(Graph, DegToCntV)

Computes an in-degree histogram: a vector of pairs (in-degree, number of nodes of such in-degree). The results are stored in *DegToCntV*.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

- *DegToCntV*: TIntPrV, a vector of (int, int) pairs (output)
    A vector of (in-degree, number of nodes of such in-degree) pairs.

Return value:

- None


The following examples shows how to obtain the in-degree histogram for nodes in :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    DegToCntV = snap.TIntPrV()
    snap.GetInDegCnt(Graph, DegToCntV)
    for item in DegToCntV:
        print "%d nodes with in-degree %d" % (item.GetVal1(), item.GetVal2())

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    DegToCntV = snap.TIntPrV()
    snap.GetInDegCnt(Graph, DegToCntV)
    for item in DegToCntV:
        print "%d nodes with in-degree %d" % (item.GetVal1(), item.GetVal2())

    Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    DegToCntV = snap.TIntPrV()
    snap.GetInDegCnt(Graph, DegToCntV)
    for item in DegToCntV:
        print "%d nodes with in-degree %d" % (item.GetVal1(), item.GetVal2())
