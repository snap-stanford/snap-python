GetNodeTriads
'''''''''''''

.. function:: GetNodeTriads(Graph, NId)

Returns number of triads a node *NId* participates in. Considers the graph as undirected. 

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network.

- *NId*: int (input)
    A node id in *Graph*.

Return value:

- int
    The number of triads node *NId* participates in.

The following example shows the number of triads for nodes in 
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    for NI in Graph.Nodes():
        print '%d %d' % (NI.GetId(), snap.GetNodeTriads(Graph, NI.GetId()))
    
    UGraph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    for NI in UGraph.Nodes():
        print '%d %d' % (NI.GetId(), snap.GetNodeTriads(Graph, NI.GetId()))

    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    for NI in Network.Nodes():
        print '%d %d' % (NI.GetId(), snap.GetNodeTriads(Graph, NI.GetId()))

