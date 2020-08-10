GetShortPath (SWIG)
'''''''''''''''''''

.. function:: GetShortPath(Graph, SrcNId, DstNId, IsDir=False)

Returns the length of the shortest path from node *SrcNId* to node *DstNId*.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network.

- *SrcNId*: int (input)
    Node id for source node.

- *DstNId*: int (input)
    Node id for destination node.

- *IsDir*: bool (input)
    Indicates whether the edges should be considered directed or undirected.

Return value:

- int
    Number of edges traversed in shortest path from *SrcNId* to *DstNId*.


The following example shows how to find shortest path for nodes in 
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    Length = GetShortPath(Graph, 1, 100)
    print("Shortest Path from node 1 to node 100 is %d edges" % Length)

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    Length = GetShortPath(UGraph, 1, 100)
    print("Shortest Path from node 1 to node 100 is %d edges" % Length)

    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    Length = GetShortPath(Network, 1, 100)
    print("Shortest Path from node 1 to node 100 is %d edges" % Length)

