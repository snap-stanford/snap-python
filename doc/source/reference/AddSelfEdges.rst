AddSelfEdges
''''''''''''


.. function:: AddSelfEdges(Graph)

Adds a self-edge for every node in *Graph*.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

Return value:

- None


The following example shows how to add self edges to every node in
:class:`PNGraph`, :class:`PUNGraph`, and :class:`PNEANet`::

    import snap

    ### PNGraph
    print "--- PNGraph ---"
    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)

    # Print starting number of edges, nodes
    print "Starting total edges: %d" % Graph.GetEdges()
    print "Starting total nodes: %d" % Graph.GetNodes()

    # Add Self Edges
    snap.AddSelfEdges(Graph)
    print "Ending total edges: %d" % Graph.GetEdges()
    NumSelfEdges = 0
    for NI in Graph.Nodes():
        if Graph.IsEdge(NI.GetId(),NI.GetId()): 
            NumSelfEdges += 1
    print "Number of self edges: %d" % NumSelfEdges




    ### PUNGraph
    print "--- PUNGraph ---"
    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)

    # Print starting number of edges, nodes
    print "Starting total edges: %d" % Graph.GetEdges()
    print "Starting total nodes: %d" % Graph.GetNodes()

    # Add Self Edges
    snap.AddSelfEdges(Graph)
    print "Ending total edges: %d" % Graph.GetEdges()
    NumSelfEdges = 0
    for NI in Graph.Nodes():
        if Graph.IsEdge(NI.GetId(),NI.GetId()): 
            NumSelfEdges += 1
    print "Number of self edges: %d" % NumSelfEdges




    ### PNEANet
    print "--- PNEANet ---"
    Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)

    # Print starting number of edges, nodes
    print "Starting total edges: %d" % Graph.GetEdges()
    print "Starting total nodes: %d" % Graph.GetNodes()

    # Add Self Edges
    snap.AddSelfEdges(Graph)
    print "Ending total edges: %d" % Graph.GetEdges()
    NumSelfEdges = 0
    for NI in Graph.Nodes():
        if Graph.IsEdge(NI.GetId(),NI.GetId()): 
            NumSelfEdges += 1
    print "Number of self edges: %d" % NumSelfEdges
