GetShortPath
''''''''''''

.. function:: GetShortPath(SrcNId, DstNId, IsDir=False)

A graph method that returns the length of the shortest path from node *SrcNId* to node *DstNId*.

Parameters:

- *SrcNId*: int
    Node id for source node.

- *DstNId*: int
    Node id for destination node.

- (optional) *IsDir*: bool
    Indicates whether the edges should be considered directed or undirected.

Return value:

- int
    Number of edges traversed in shortest path from *SrcNId* to *DstNId*.


The following example shows how to find shortest path for nodes in 
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    Length = Graph.GetShortPath(1, 100)
    print("Shortest Path from node 1 to node 100 is %d edges" % Length)

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    Length = UGraph.GetShortPath(1, 100)
    print("Shortest Path from node 1 to node 100 is %d edges" % Length)

    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    Length = Network.GetShortPath(1, 100)
    print("Shortest Path from node 1 to node 100 is %d edges" % Length)

