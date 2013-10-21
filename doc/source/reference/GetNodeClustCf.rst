GetNodeClustCf
''''''''''''''
.. note::

    This page is a draft and under revision.


.. function:: GetNodeClustCf(Graph, NId) 

Returns clustering coefficient of a particular node. Considers the graph as undirected.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

- *NId*: int (input)
    Node ID

Return value:

- float
    Clustering coefficient of a particular node

For more info see: http://en.wikipedia.org/wiki/Clustering_coefficient

The following example shows how to calculate clustering coefficient of a particular node in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    G1 = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    snap.GetNodeClustCf(G1, 50)

    G2 = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    snap.GetNodeClustCf(G2, 50)

    G3 = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    snap.GetNodeClustCf(G3, 50)
