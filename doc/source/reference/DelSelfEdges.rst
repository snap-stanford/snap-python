DelSelfEdges
''''''''''''

.. function:: DelSelfEdges ()

A graph method to remove all the self-edges from a graph.

Parameters:

- None

Return value:

- None


The following example shows how to delete self-edges in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.TNGraph, 100, 1000)
    Graph.AddSelfEdges()
    for NI in Graph.Nodes():
        if Graph.IsEdge(NI.GetId(),NI.GetId()): 
            print("Self-edge on node %d" % NI.GetId())
    Graph.DelSelfEdges()
    for NI in Graph.Nodes():
        if Graph.IsEdge(NI.GetId(),NI.GetId()): 
            print("Self-edge on node %d" % NI.GetId())

    UGraph = snap.GenRndGnm(snap.TNGraph, 100, 1000)
    UGraph.AddSelfEdges()
    for NI in UGraph.Nodes():
        if UGraph.IsEdge(NI.GetId(),NI.GetId()): 
            print("Self-edge on node %d" % NI.GetId())
    UGraph.DelSelfEdges()
    for NI in UGraph.Nodes():
        if UGraph.IsEdge(NI.GetId(),NI.GetId()): 
            print("Self-edge on node %d" % NI.GetId())

    Network = snap.GenRndGnm(snap.TNGraph, 100, 1000)
    Network.AddSelfEdges()
    for NI in Network.Nodes():
        if Network.IsEdge(NI.GetId(),NI.GetId()): 
            print("Self-edge on node %d" % NI.GetId())
    Network.DelSelfEdges()
    for NI in Network.Nodes():
        if Network.IsEdge(NI.GetId(),NI.GetId()): 
            print("Self-edge on node %d" % NI.GetId())
