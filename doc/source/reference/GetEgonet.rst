GetEgonet
'''''''''

.. function:: GetEgonet(NId)

A graph method that returns an ego network of the node *NId* and the number of connecting edges. The ego network includes the node *NId*, its neighbours, and all the edges between them. Connecting edges are the edges between a node in the ego network and a node not in the network. The method is supported for :class:`TUNGraph` and :class:`TNGraph`. For :class:`TUNGraph`, connecting edges is a single value, for :class:`TNGraph`, connecting edges is represented by a pair of incoming and outgoind edges from the ego network.

Parameters:

- *NId*: int
    Id of the center node of the ego network.

Return value:

- graph
    A graph of the same type as the input graph, containing the ego network for *NId*.

- edges: int
    The number of connecting edges from the ego network. For :class:`TNGraph`, only incoming edges are counted here.

- edges: int (returned only for :class:`TNGraph`):
    The number of outgoing connecting edges from the ego network.


The following example shows how to create a subgraph for nodes in 
:class:`TUNGraph`, and :class:`TNGraph`::

    import snap

    UGraph = snap.GenRndGnm(snap.TUNGraph, 100, 1000)
    Egonet, edges = UGraph.GetEgonet(0)

    NGraph = snap.GenRndGnm(snap.TNGraph, 100, 1000)
    Egonet, edges_in, edges_out = NGraph.GetEgonet(0)

