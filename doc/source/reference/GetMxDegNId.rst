GetMxDegNId
'''''''''''
.. note::

    This page is a draft and under revision.


.. function:: TSnap::GetMxDegNId(Graph)   

Returns a randomly chosen node from all the nodes with the maximum degree.

Parameters:

- *Graph*: PGraph (input)
    Any graph, directed or undirected

Return value:

- *NodeID*: int (output)
    A randomly chosen node from all the nodes with the maximum degree

For more info see: http://snap.stanford.edu/snap/doc/snapdev-ref/d3/d73/namespaceTSnap.html#afbc8b8ef6cc8d4b8a0de1faad0c0a912

The following example shows how to find a node with maximum degree for nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    G1 = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    id1 = snap.GetMxDegNId(G1)
    print id1

    G2 = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    id2 = snap.GetMxDegNId(G2)
    print id2

    G3 = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    id3 = snap.GetMxDegNId(G3)
    print id3

