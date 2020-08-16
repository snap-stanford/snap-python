GetBiConSzCnt
'''''''''''''

.. function:: GetBiConSzCnt()

A graph method for undirected graphs that returns a distribution of bi-connected component sizes.  A bi-connected component is a maximal subgraph with no articulation points.

Parameters:

- None

Return value:

- *SzCntV*: :class:`TIntPrV`, a vector of (int, int) pairs
    A vector of pairs (number of nodes in the bi-component, number of such components).


The following example shows how to calculate bi-connected component size
distribution in :class:`TUNGraph`::

    import snap

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 100)
    SzCntV = UGraph.GetBiConSzCnt()
    for item in SzCntV:
        print("%d, %d" % (item.GetVal1(), item.GetVal2()))
