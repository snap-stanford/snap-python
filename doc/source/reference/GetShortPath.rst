GetShortPath
''''''''''''

.. function:: Length = GetShortPath(Graph, SrcNId, DstNId)

Returns the length of the shortest path from node SrcNId to node DstNId.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

- *SrcNId*: int (input)
    Node ID for source node 

- *DstNId*: int (input)
    Node ID for destination node

Return value:

- *Length*: int (output)
    Number of edges traversed in shortest path from SrcNId to DstNId

The following example shows how to find shortest path for nodes in 
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    Length = GetShortPath(Graph, 1, 100)
    print "Shortest Path from node 1 to node 100 is %d edges" % Length

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    Length = GetShortPath(Graph, 1, 100)
    print "Shortest Path from node 1 to node 100 is %d edges" % Length

    Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    Length = GetShortPath(Graph, 1, 100)
    print "Shortest Path from node 1 to node 100 is %d edges" % Length

