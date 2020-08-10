GetMxOutDegNId
''''''''''''''

.. function:: GetMxOutDegNId()

A method that returns the node id of a randomly chosen node from all the nodes in *Graph* with the maximum out-degree.

Parameters:

- None

Return value:

- int
    The node id of a randomly chosen node from all the nodes in *Graph* with the maximum out-degree.


The following example shows how to use :func:`GetMxOutDegNId` with
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    NId1 = Graph.GetMxOutDegNId()
    print(NId1)

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    NId2 = UGraph.GetMxOutDegNId()
    print(NId2)

    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    NId3 = Network.GetMxOutDegNId()
    print(NId3)

