GetInEgonetSub
''''''''''''''

.. function:: GetInEgonetSub(NId, H, N = 2, P = -1.0)

A graph method that returns a sampled *H* hop in-ego network of the node *NId*. A sampled *H* hop in-ego network includes the node *NId*, a sample of its in-neighbours and edges that connect them to the origin node, then samples of all their in-neighbours and edges and so on until *H* hop neighbours. The sampling is specified by the *N* and *P* parameters. If *P* is -1.0, then *N* determines the maximum number of neighbours added to the in-ego network for each node. If *P* is different than -1.0, then it determines the percentage of added neighbours. For example, if *P* is 0.5, then half of the neighbours will be added to the in-ego network for each node. The neighbours are selected randomly.

Parameters:

- *NId*: int
    Id of the center node of the ego network.

- *H*: int
    The number of hops for the ego network.

- (optional) *N*: int
    The maximum number of neighbours selected. Default value is 2. It has no effect, is *P* is different from -1.0.

- (optional) *P*: float
    The percentage of neighbours selected, between 0.0 and 1.0. Default value is -1.0, which means that the parameter has no effect.

Return value:

- graph
    A graph of the same type as the input graph, containing the in-ego network for *NId*.

The following example shows how to create a subgraph for nodes in 
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    NGraph = snap.GenRndGnm(snap.TNGraph, 100, 1000)
    InEgonet = NGraph.GetInEgonetSub(0, 2, 3)

    UGraph = snap.GenRndGnm(snap.TUNGraph, 100, 1000)
    InEgonet = UGraph.GetInEgonetSub(3, 1, 3)

    Network = snap.GenRndGnm(snap.TNEANet, 100, 1000)
    InEgonet = Network.GetInEgonetSub(10, 3, 0, 0.4)

