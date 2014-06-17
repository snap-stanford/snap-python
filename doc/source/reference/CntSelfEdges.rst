CntSelfEdges
''''''''''''

.. function:: CntSelfEdges (Graph)

Returns the number of self edges in the graph *Graph*. 

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network.

Return value:

- int
    The number of self edges in *Graph*.


The following example shows how to calculate the number of self edges in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    Count = snap.CntSelfEdges(Graph)
    print "Directed Graph: Count of self edges is %d" % Count

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    Count = snap.CntSelfEdges(UGraph)
    print "Undirected Graph: Count of self edges is %d" % Count

    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    Count = snap.CntSelfEdges(Network)
    print "Network Graph: Count of self edges is %d" % Count
