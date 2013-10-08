CntSelfEdges
''''''''''''

.. function:: int CntSelfEdges (Graph)

Counts the number of self-edges in a graph. Edge (u,u) is a self-edge.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

Return value:

- (int) Number of self-edges in the graph.

The following example shows how count number of self edges in :class:`Graph`::

    import snap

    G1 = snap.TUNGraph.New()
    G1.AddNode(0)
    G1.AddNode(1)
    G1.AddEdge(0,1)
    G1.AddEdge(1,1)

    for NI in G1.Nodes():
        print "node: %d, out-degree %d, in-degree %d" % ( NI.GetId(), NI.GetOutDeg(), NI.GetInDeg())

    print snap.CntSelfEdges(G1)
