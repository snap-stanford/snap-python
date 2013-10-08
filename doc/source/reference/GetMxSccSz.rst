GetMxSccSz
'''''''''''
.. note::

    This page is a draft and under revision.


.. function:: GetMxSccSz(Graph)

Returns the fraction of nodes in the largest strongly connected component of a Graph.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

Return value:

- *GetMxSccSz*: double (output)
    The fraction of nodes in the largest strongly connected component of a graph.

The following example shows how to calculate PageRank scores for nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    print snap.GetMxSccSz(Graph)

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    print snap.GetMxSccSz(Graph)

    Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    print snap.GetMxSccSz(Graph)
