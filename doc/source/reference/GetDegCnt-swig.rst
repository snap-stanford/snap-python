GetDegCnt (SWIG)
''''''''''''''''''''''

.. function:: GetDegCnt(Graph, DegToCntV)
   :noindex:

Computes a degree histogram: a vector of pairs (degree, number of nodes of such degree). The results are stored in *DegToCntV*.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network.

- *DegToCntV*: :class:`TIntPrV`, a vector of (int, int) pairs (output)
    A vector of (degree, number of nodes of such degree) pairs.

Return Value:

- None


The following examples shows how to obtain the degree histogram for nodes in :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    DegToCntV = snap.TIntPrV()
    snap.GetDegCnt(Graph, DegToCntV)
    for item in DegToCntV:
        print("%d nodes with degree %d" % (item.GetVal2(), item.GetVal1()))

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    DegToCntV = snap.TIntPrV()
    snap.GetDegCnt(UGraph, DegToCntV)
    for item in DegToCntV:
        print("%d nodes with degree %d" % (item.GetVal2(), item.GetVal1()))

    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    DegToCntV = snap.TIntPrV()
    snap.GetDegCnt(Network, DegToCntV)
    for item in DegToCntV:
        print("%d nodes with degree %d" % (item.GetVal2(), item.GetVal1()))
