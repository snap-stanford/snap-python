GetMxInDegNId
'''''''''''''

.. function:: GetMxInDegNId(Graph)

Returns the node id of a randomly chosen node from all the nodes in *Graph* with the maximum in-degree.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

Return value:

- int
    The node id of a randomly chosen node from all the nodes in *Graph* with the maximum in-degree

The following example shows how to use :func:`GetMxInDegNId` with
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    NId1 = snap.GetMxInDegNId(Graph)
    print NId1

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    NId2 = snap.GetMxInDegNId(Graph)
    print NId2

    Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    NId3 = snap.GetMxInDegNId(Graph)
    print NId3

