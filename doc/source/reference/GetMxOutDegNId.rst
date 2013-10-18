GetMxOutDegNId
''''''''''''''
.. note::

    This page is a draft and under revision.


.. function:: GetMxOutDegNId(Graph)

Returns the node id of a randomly chosen node from all the nodes in *Graph* with the maximum out-degree.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

Return value:

- int

The following example shows how to use :func:`GetMxOutDegNId` with
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    NodeMaxDeg = snap.GetMxOutDegNId(Graph)
    print NodeMaxDeg

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    NodeMaxDeg = snap.GetMxOutDegNId(Graph)
    print NodeMaxDeg

    Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    NodeMaxDeg = snap.GetMxOutDegNId(Graph)
    print NodeMaxDeg
