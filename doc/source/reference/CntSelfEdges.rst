CntSelfEdges
''''''''''''


.. function:: CntSelfEdges (Graph)

Returns the number of self-edges in the graph *Graph*. Edge (u,u) is a self-edge.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

Return value:

- int
    The number of self edges in *Graph*.

The following example shows how to count the number of self edges in :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::.

    import snap

    Graph = snap.TNGraph.New()
    Graph.AddNode(0)
    Graph.AddEdge(0,0)
    print snap.CntSelfEdges(Graph)

    Graph = snap.TUNGraph.New()
    Graph.AddNode(0)
    Graph.AddEdge(0,0)
    print snap.CntSelfEdges(Graph)

    Graph = snap.TNEANet.New()
    Graph.AddNode(0)
    Graph.AddEdge(0,0)
    print snap.CntSelfEdges(Graph)
