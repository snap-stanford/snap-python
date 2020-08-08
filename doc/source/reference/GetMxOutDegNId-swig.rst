GetMxOutDegNId (SWIG)
'''''''''''''''''''''

.. function:: GetMxOutDegNId(Graph)

Returns the node id of a randomly chosen node from all the nodes in *Graph* with the maximum out-degree.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network.

Return value:

- int
    The node id of a randomly chosen node from all the nodes in *Graph* with the maximum out-degree.


The following example shows how to use :func:`GetMxOutDegNId` with
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    NId1 = snap.GetMxOutDegNId(Graph)
    print(NId1)

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    NId2 = snap.GetMxOutDegNId(UGraph)
    print(NId2)

    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    NId3 = snap.GetMxOutDegNId(Network)
    print(NId3)

