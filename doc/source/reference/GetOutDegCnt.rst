GetOutDegCnt
''''''''''''


.. function:: GetOutDegCnt(Graph, DegToCntV)

Computes an out-degree histogram: a vector of pairs (out-degree, number of nodes of such out-degree). The results are stored in *DegToCntV*.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

- *DegToCntV*: TIntPrV, vector of (int, int) pairs (output)
    A vector of (out-degree, number of nodes of such out-degree) pairs

Return value:

- None


The following examples shows how to obtain the degree histogram for nodes in :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    DegToCntV = snap.TIntPrV()
    snap.GetOutDegCnt(Graph, DegToCntV)
    for item in DegToCntV:
        print item.GetVal1(), item.GetVal2()

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    DegToCntV = snap.TIntPrV()
    snap.GetOutDegCnt(Graph, DegToCntV)
    for item in DegToCntV:
        print item.GetVal1(), item.GetVal2()

    Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    DegToCntV = snap.TIntPrV()
    snap.GetOutDegCnt(Graph, DegToCntV)
    for item in DegToCntV:
        print item.GetVal1(), item.GetVal2()
