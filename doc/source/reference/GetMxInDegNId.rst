GetMxInDegNId
'''''''''''''

.. function:: GetMxInDegNId()

A method that returns the node id of a randomly chosen node from all the nodes in *Graph* with the maximum in-degree.

Parameters:

- None

Return value:

- int
    The node id of a randomly chosen node from all the nodes in *Graph* with the maximum in-degree.


The following example shows how to use :func:`GetMxInDegNId` with
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.TNGraph, 100, 1000)
    NId1 = Graph.GetMxInDegNId()
    print(NId1)

    UGraph = snap.GenRndGnm(snap.TUNGraph, 100, 1000)
    NId2 = UGraph.GetMxInDegNId()
    print(NId2)

    Network = snap.GenRndGnm(snap.TNEANet, 100, 1000)
    NId3 = Network.GetMxInDegNId()
    print(NId3)

