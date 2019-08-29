GetFarnessCentr
'''''''''''''''

.. function:: GetFarnessCentr(Graph, NId, Normalized=True, IsDir=False)

Returns farness centrality of a given node *NId* in *Graph*. Farness centrality of a node is the average shortest path length to all other nodes that reside in the same connected component as the given node.

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
    The farness centrality of the node *NId* in *Graph*.


The following example shows how to get the farness centrality for nodes in 
:class:`TNGraph`,
:class:`TUNGraph`, and
:class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    for NI in Graph.Nodes():
        FarCentr = snap.GetFarnessCentr(Graph, NI.GetId())
        print("node: %d centrality: %f" % (NI.GetId(), FarCentr))

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    for NI in UGraph.Nodes():
        FarCentr = snap.GetFarnessCentr(UGraph, NI.GetId())
        print("node: %d centrality: %f" % (NI.GetId(), FarCentr))

    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    for NI in Network.Nodes():
        FarCentr = snap.GetFarnessCentr(Network, NI.GetId())
        print("node: %d centrality: %f" % (NI.GetId(), FarCentr))

