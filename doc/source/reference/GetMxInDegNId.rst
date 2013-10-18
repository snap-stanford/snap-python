GetMxInDegNId
'''''''''''''
.. note::

    This page is a draft and under revision.


.. function:: GetMxInDegNId(Graph)

Returns the node id of a randomly chosen node from all the nodes in *Graph* with the maximum in-degree.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

Return value:

- int

The following example shows how to use :func:`GetMxInDegNId` with
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    id1 = snap.GetMxInDegNId(Graph)
    print id1

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    id2 = snap.GetMxInDegNId(Graph)
    print id2

    Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    id3 = snap.GetMxInDegNId(Graph)
    print id3
