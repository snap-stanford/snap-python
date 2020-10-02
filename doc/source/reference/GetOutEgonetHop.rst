GetOutEgonetHop
'''''''''''''''

.. function:: GetOutEgonetHop(NId, H)

A graph method that returns an *H* hop out-ego network of the node *NId*. The *H* hop out-ego network includes the node *NId*, its out-neighbours and edges that connect them to the origin node, then all their out-neighbours and edges and so on until *H* hop neighbours.

Parameters:

- *NId*: int
    Id of the center node of the ego network.

- *H*: int
    The number of hops for the ego network.

Return value:

- graph
    A graph of the same type as the input graph, containing the out-ego network for *NId*.

The following example shows how to create a subgraph for nodes in 
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    NGraph = snap.GenRndGnm(snap.TNGraph, 100, 1000)
    OutEgonet = NGraph.GetOutEgonetHop(0, 2)

    UGraph = snap.GenRndGnm(snap.TUNGraph, 100, 1000)
    OutEgonet = UGraph.GetOutEgonetHop(3, 1)

    Network = snap.GenRndGnm(snap.TNEANet, 100, 1000)
    OutEgonet = Network.GetOutEgonetHop(10, 3)

