GetDegCnt
'''''''''''''''


.. function:: GetDegCnt(Graph, DegToCntV)

Computes a degree histogram: a vector of pairs (degree, number of nodes of such degree). The results are stored in *DegToCntV*.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

- *DegToCntV*: TIntPrV, a vector of (int, int) pairs (output)
    A vector of (degree, number of nodes of such degree) pairs.

Return Value:

- None


The following examples shows how to obtain the degree histogram for nodes in :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    DegToCntV = snap.TIntPrV()
    snap.GetDegCnt(Graph, DegToCntV)
    for item in DegToCntV:
        print "%s nodes with degree %s" % (item.GetVal1(), item.GetVal2())

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    DegToCntV = snap.TIntPrV()
    snap.GetDegCnt(Graph, DegToCntV)
    for item in DegToCntV:
        print "%s nodes with degree %s" % (item.GetVal1(), item.GetVal2())

    Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    DegToCntV = snap.TIntPrV()
    snap.GetDegCnt(Graph, DegToCntV)
    for item in DegToCntV:
        print "%s nodes with degree %s" % (item.GetVal1(), item.GetVal2())
