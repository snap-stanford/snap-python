GetClosenessCentr
'''''''''''''''''

.. function:: GetClosenessCentr(Graph, NId, Normalized=True, IsDir=False)

Returns closeness centrality of a given node *NId* in *Graph*. Closeness centrality is equal to 1/farness centrality.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network.

- *NId*: int (input)
    A node id in *Graph*.

- *Normalized*: bool (input)
    Output should be normalized (*True*) or not (*False*).

- *IsDir*: bool (input)
    Indicates whether the edges should be considered directed (*True*) or undirected (*False*).


Return value:

- float
    The closeness centrality of the node *NId* in *Graph*.


The following example shows how to get the closeness centrality for nodes in 
:class:`TNGraph`,
:class:`TUNGraph`, and
:class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    for NI in Graph.Nodes():
        CloseCentr = snap.GetClosenessCentr(Graph, NI.GetId())
        print "node: %d centrality: %f" % (NI.GetId(), CloseCentr)

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    for NI in UGraph.Nodes():
        CloseCentr = snap.GetClosenessCentr(UGraph, NI.GetId())
        print "node: %d centrality: %f" % (NI.GetId(), CloseCentr)

    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    for NI in Network.Nodes():
        CloseCentr = snap.GetClosenessCentr(Network, NI.GetId())
        print "node: %d centrality: %f" % (NI.GetId(), CloseCentr)
