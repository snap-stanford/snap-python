GetOutDegCnt
''''''''''''
.. note::

    This page is a draft and under revision.


.. function:: GetOutDegCnt(Graph, DegToCntV)

Computes the number of out degrees of each node and saves the result in a vector of (out-degree, number of nodes of such out-degree) pairs.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

- *DegToCntV*: vector of (int, int) pairs (output)
    A vector of (out-degree, number of nodes of such out-degree) pairs

Return value:

- None

For more information, see http://en.wikipedia.org/wiki/Directed_graph#Indegree_and_outdegree.

Note that in an undirected graph of N nodes, each edge is counted twice, so the number of nodes of all out-degrees will be 2*N.

The following example shows how to calculate out degree data for
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

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
