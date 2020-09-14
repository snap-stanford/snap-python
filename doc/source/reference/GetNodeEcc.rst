GetNodeEcc
'''''''''''

.. function:: GetNodeEcc(NId, IsDir=False)

A graph method that returns node eccentricity, the largest shortest-path distance from the node *NId* to any other node.

Parameters:

- *NId*: int
    A node id.

- (optional) *IsDir*: bool
    Indicates whether the edges should be considered directed or undirected.

Return value:

- int
    The eccentricity of node *NId*.

The following example shows how to calculate eccentricity for nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap
    
    Graph = snap.GenRndGnm(snap.TNGraph, 10, 30)
    for NI in Graph.Nodes():
        print(NI.GetId(), Graph.GetNodeEcc(NI.GetId(), True))
    
    UGraph = snap.GenRndGnm(snap.TUNGraph, 10, 30)
    for NI in UGraph.Nodes():
        print(NI.GetId(), UGraph.GetNodeEcc(NI.GetId(), False))

    Network = snap.GenRndGnm(snap.TNEANet, 10, 30)
    for NI in Network.Nodes():
        print(NI.GetId(), Network.GetNodeEcc(NI.GetId(), True))

