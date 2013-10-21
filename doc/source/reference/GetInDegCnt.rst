GetInDegCnt
'''''''''''
.. note::

    This page is a draft and under revision.


.. function:: GetInDegCnt(Graph, DegToCntV)

Computes an in-degree histogram: a set of pairs (in-degree, number of nodes of such in-degree). The results are stored in *DegToCntV*.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

- *DegToCntV*: TIntPrV, a vector of (int, int) pairs (output)
    A vector of (in-degree, number of nodes of such out-degree) pairs.

Return value:

- None

The following example shows how to use :func:`InDegCnt` with nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    DegToCntV = snap.TIntPrV()
    snap.GetInDegCnt(Graph, DegToCntV)
    for pair in DegToCntV:
      print pair.GetVal1(), pair.GetVal2()

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    DegToCntV = snap.TIntPrV()
    snap.GetInDegCnt(Graph, DegToCntV)
    for pair in DegToCntV:
      print pair.GetVal1(), pair.GetVal2()

    Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    DegToCntV = snap.TIntPrV()
    snap.GetInDegCnt(Graph, DegToCntV)
    for pair in DegToCntV:
      print pair.GetVal1(), pair.GetVal2()