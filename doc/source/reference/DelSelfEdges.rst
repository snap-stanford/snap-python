DelSelfEdges
''''''''''''

.. function:: DelSelfEdges (Graph)

Removes all the self-edges from *Graph*.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or network.

Return value:

- None


The following example shows how to delete self-edges in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    snap.AddSelfEdges(Graph)
    for NI in Graph.Nodes():
        if Graph.IsEdge(NI.GetId(),NI.GetId()): 
            print("Self-edge on node %d" % NI.GetId())
    snap.DelSelfEdges(Graph)
    for NI in Graph.Nodes():
        if Graph.IsEdge(NI.GetId(),NI.GetId()): 
            print("Self-edge on node %d" % NI.GetId())

    UGraph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    snap.AddSelfEdges(UGraph)
    for NI in UGraph.Nodes():
        if UGraph.IsEdge(NI.GetId(),NI.GetId()): 
            print("Self-edge on node %d" % NI.GetId())
    snap.DelSelfEdges(UGraph)
    for NI in UGraph.Nodes():
        if UGraph.IsEdge(NI.GetId(),NI.GetId()): 
            print("Self-edge on node %d" % NI.GetId())

    Network = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    snap.AddSelfEdges(Network)
    for NI in Network.Nodes():
        if Network.IsEdge(NI.GetId(),NI.GetId()): 
            print("Self-edge on node %d" % NI.GetId())
    snap.DelSelfEdges(Network)
    for NI in Network.Nodes():
        if Network.IsEdge(NI.GetId(),NI.GetId()): 
            print("Self-edge on node %d" % NI.GetId())
