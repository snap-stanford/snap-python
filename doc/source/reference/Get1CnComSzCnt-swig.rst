Get1CnComSzCnt (SWIG)
'''''''''''''''''''''

.. function:: Get1CnComSzCnt (Graph, SzCntV)

Returns a distribution of sizes of 1-components: maximal connected components of that can be disconnected from the *Graph* by removing a single edge.

Parameters:

- *Graph*: undirected graph (input)
    A Snap.py undirected graph.

- *SzCntV*: :class:`TIntPrV`, a vector of (int, int) pairs (output)
    A vector of pairs (number of nodes in the 1-component, number of such components).

Return value:

- None


The following example shows how to get distribution of sizes of 1-components in  :class:`TUNGraph`::

    import snap

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 100)
    szCntV = snap.TIntPrV()

    snap.Get1CnComSzCnt(UGraph, szCntV)
    for item in szCntV:
        print("%d, %d" % (item.GetVal1(), item.GetVal2()))
