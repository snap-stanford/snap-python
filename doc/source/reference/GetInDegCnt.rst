GetInDegCnt
'''''''''''

.. function:: GetInDegCnt(Graph, DegToCntV)

Returns an in-degree histogram: a set of pairs (in-degree, number of nodes of such in-degree).

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

- *DegToCntV*: a vector of int pairs (output)
    An in-degree histogram. Pairs are in-degree, number of nodes of such in-degree.

Return value:

- None

The following example shows how to calculate InDegCnt for nodes in
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