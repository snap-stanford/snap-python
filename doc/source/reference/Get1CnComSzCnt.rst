Get1CnComSzCnt
''''''''''''''

.. function:: Get1CnComSzCnt ()

A graph method for undirected graphs that returns a distribution of sizes of 1-components: maximal connected components of that can be disconnected from a graph by removing a single edge.

Parameters:

- None

Return value:

- *SzCntV*: :class:`TIntPrV`, a vector of (int, int) pairs
    A vector of pairs (number of nodes in the 1-component, number of such components).


The following example shows how to get distribution of sizes of 1-components in  :class:`TUNGraph`::

    import snap

    UGraph = snap.GenRndGnm(snap.TUNGraph, 100, 100)
    szCntV = UGraph.Get1CnComSzCnt()
    for item in szCntV:
        print("%d, %d" % (item.GetVal1(), item.GetVal2()))
