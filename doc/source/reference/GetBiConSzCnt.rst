GetBiConSzCnt
'''''''''''

.. function:: GetBiConSzCnt(Graph, SzCntV)

Returns a distribution of bi-connected component sizes.

Parameters:

- *Graph*: Undirected graph (input)
    A Snap.py undirected graph

- *SzCntV*: Vector of integer pairs (output)
    A set of pairs (number of nodes in the bi-component, number of such components)

Return value:

- None

For more info see: http://en.wikipedia.org/wiki/Biconnected_graph

The following example shows how to calculate bi-connected component size
distribution in :class:`PUNGraph`::

    import snap

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 100)
    szCntV = snap.TIntPrV()

    snap.GetBiConSzCnt(Graph, szCntV)
    for item in szCntV:
        print "{} {}".format(item.GetVal1(), item.GetVal2())
