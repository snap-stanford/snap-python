GetNodeTriads
'''''''''''''

.. function:: GetNodeTriads(NId)

A graph method that returns the number of triads a node *NId* participates in. Considers the graph as undirected. 

Parameters:

- *NId*: int
    A node id in the graph.

Return value:

- int
    The number of triads node *NId* participates in.

The following example shows how to calculate the number of triads for nodes in 
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    for NI in Graph.Nodes():
        print('%d %d' % (NI.GetId(), Graph.GetNodeTriads(NI.GetId())))
    
    UGraph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    for NI in UGraph.Nodes():
        print('%d %d' % (NI.GetId(), UGraph.GetNodeTriads(NI.GetId())))

    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    for NI in Network.Nodes():
        print('%d %d' % (NI.GetId(), Network.GetNodeTriads(NI.GetId())))

