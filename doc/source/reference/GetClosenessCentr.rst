GetClosenessCentr
'''''''''''''''''

.. function:: GetClosenessCentr(NId, Normalized=True, IsDir=False)

A graph method that returns closeness centrality of a given node *NId*. Closeness centrality is equal to 1/farness centrality.

Parameters:

- *NId*: int
    A node id in *Graph*.

- (optional) *Normalized*: bool
    Output should be normalized (*True*) or not (*False*).

- (optional) *IsDir*: bool
    Indicates whether the edges should be considered directed (*True*) or undirected (*False*).


Return value:

- float
    The closeness centrality of the node *NId*.


The following example shows how to get the closeness centrality for nodes in 
:class:`TNGraph`,
:class:`TUNGraph`, and
:class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    for NI in Graph.Nodes():
        CloseCentr = Graph.GetClosenessCentr(NI.GetId())
        print("node: %d centrality: %f" % (NI.GetId(), CloseCentr))

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    for NI in UGraph.Nodes():
        CloseCentr = UGraph.GetClosenessCentr(NI.GetId())
        print("node: %d centrality: %f" % (NI.GetId(), CloseCentr))

    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    for NI in Network.Nodes():
        CloseCentr = Network.GetClosenessCentr(NI.GetId())
        print("node: %d centrality: %f" % (NI.GetId(), CloseCentr))
