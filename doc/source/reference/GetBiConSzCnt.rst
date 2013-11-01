GetBiConSzCnt
'''''''''''''


.. function:: GetBiConSzCnt(Graph, SzCntV)

Returns a distribution of bi-connected component sizes.  A bi-connected component is a maximal subgraph with no articulation points.


Parameters:

- *Graph*: undirected graph (input)
    A Snap.py undirected graph

- *SzCntV*: TIntPrV, a vector of (int, int) pairs (output)
    A vector of pairs (number of nodes in the bi-component, number of such components)

Return value:

- None

For more info see: http://en.wikipedia.org/wiki/Biconnected_graph

The following example shows how to calculate bi-connected component size
distribution in :class:`TUNGraph`::

    import snap

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 100)
    szCntV = snap.TIntPrV()

    snap.GetBiConSzCnt(Graph, szCntV)
    for item in szCntV:
        print "%d, %d" % (item.GetVal1(), item.GetVal2())
