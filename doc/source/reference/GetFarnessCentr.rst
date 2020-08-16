GetFarnessCentr
'''''''''''''''

.. function:: GetFarnessCentr(NId, Normalized=True, IsDir=False)

A graph method that returns farness centrality of a given node *NId*. Farness centrality of a node is the average shortest path length to all other nodes that reside in the same connected component as the given node.

Parameters:

- *NId*: int
    A node id.

- (optional) *Normalized*: bool
    Output should be normalized (*True*) or not (*False*).

- (optional) *IsDir*: bool
    Indicates whether the edges should be considered directed (*True*) or undirected (*False*).

Return value:

- float
    The farness centrality of the node *NId*.


The following example shows how to get the farness centrality for nodes in 
:class:`TNGraph`,
:class:`TUNGraph`, and
:class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    for NI in Graph.Nodes():
        FarCentr = Graph.GetFarnessCentr(NI.GetId())
        print("node: %d centrality: %f" % (NI.GetId(), FarCentr))

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    for NI in UGraph.Nodes():
        FarCentr = UGraph.GetFarnessCentr(NI.GetId())
        print("node: %d centrality: %f" % (NI.GetId(), FarCentr))

    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    for NI in Network.Nodes():
        FarCentr = Network.GetFarnessCentr(NI.GetId())
        print("node: %d centrality: %f" % (NI.GetId(), FarCentr))

