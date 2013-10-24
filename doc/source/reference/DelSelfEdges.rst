DelSelfEdges
''''''''''''


.. function:: DelSelfEdges (Graph)

Removes all the self-edges from *Graph*.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or network

Return value:

- None


The following example shows how to delete self-edges in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    ### PNGraph
    print "--- PNGraph ---"
    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    Graph.AddEdge(1,1)

    # Print initial self-edges
    print "Self-edges in initial graph: "
    for NI in Graph.Nodes():
        if Graph.IsEdge(NI.GetId(),NI.GetId()): 
            print "Self-edge on node %d" % NI.GetId()

    # Remove self-edges
    snap.DelSelfEdges(Graph)
    print "Deleted self-edges"
    for NI in Graph.Nodes():
        if Graph.IsEdge(NI.GetId(),NI.GetId()): 
            print "Self-edge on node %d" % NI.GetId()




    ### PUNGraph
    print "--- PUNGraph ---"
    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    Graph.AddEdge(1,1)

    # Print initial self-edges
    print "Self-edges in initial graph: "
    for NI in Graph.Nodes():
        if Graph.IsEdge(NI.GetId(),NI.GetId()): 
            print "Self-edge on node %d" % NI.GetId()

    # Remove self-edges
    snap.DelSelfEdges(Graph)
    print "Deleted self-edges"
    for NI in Graph.Nodes():
        if Graph.IsEdge(NI.GetId(),NI.GetId()): 
            print "Self-edge on node %d" % NI.GetId()




    ### PNEANet
    print "--- PNEANet ---"
    Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    Graph.AddEdge(1,1)

    # Print initial self-edges
    print "Self-edges in initial graph: "
    for NI in Graph.Nodes():
        if Graph.IsEdge(NI.GetId(),NI.GetId()): 
            print "Self-edge on node %d" % NI.GetId()

    # Remove self-edges
    snap.DelSelfEdges(Graph)
    print "Deleted self-edges"
    for NI in Graph.Nodes():
        if Graph.IsEdge(NI.GetId(),NI.GetId()): 
            print "Self-edge on node %d" % NI.GetId()