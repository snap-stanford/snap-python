GetEgonetHop
''''''''''''

.. function:: GetEgonetHop(NId, H)

A graph method that returns an *H* hop ego network of the node *NId*. The *H* hop ego network includes the node *NId*, its *H* hop neighbours, and all the edges between them.

Parameters:

- *NId*: int
    Id of the center node of the ego network.

- *H*: int
    The number of hops for the ego network.

Return value:

- graph
    A graph of the same type as the input graph, containing the ego network for *NId*.

The following example shows how to create a subgraph for nodes in 
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    NGraph = snap.GenRndGnm(snap.TNGraph, 100, 1000)
    Egonet = NGraph.GetInEgonetHop(0, 2)

    UGraph = snap.GenRndGnm(snap.TUNGraph, 100, 1000)
    Egonet = UGraph.GetInEgonetHop(3, 1)

    Network = snap.GenRndGnm(snap.TNEANet, 100, 1000)
    Egonet = Network.GetInEgonetHop(10, 3)

