Get1CnComSzCnt
''''''''''''''
.. note::

    This page is a draft and under revision.


.. function:: Get1CnComSzCnt (Graph, SzCntV)

Distribution of sizes of 1-components, maximal number of components that can be disconnected from the Graph by removing a single edge.

Parameters:

- *Graph*: PUNGraph - undirected graph (input)
    A Snap.py undirected graph (PUNGraph)

- *SzCntV*: TIntPrV vector of (int, int) pairs (output)
    Hop count vector

Return value:

- None

We find such components as follows: Find all bridge edges, remove them from the Graph, find largest component K and add back all bridges that do not touch K. Now, find the connected components of this graph.

The following example shows how to get distribution of sizes of 1-components in  :class:`TUNGraph`::

    import snap

    # generate random graph
    Graph = snap.GenRndGnm(snap.PUNGraph, 1000, 1000)
    # initialize size count vector of pairs (int, int)
    SzCntV = snap.TIntPrV()
    snap.Get1CnComSzCnt(Graph, SzCntV)

    for item in SzCntV:
        print item.Val1(), item.Val2()
