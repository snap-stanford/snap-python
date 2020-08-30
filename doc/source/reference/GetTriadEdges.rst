GetTriadEdges
'''''''''''''

.. function:: GetTriadEdges(SampleEdges=-1)

A graph method that counts the number of edges that participate in at least one triad. Considers the graph as undirected.

Parameters:

- (Optional) *SampleEdges*: int
    If *SampleEdges* is -1 (default value), then compute triads for all the edges. Otherwise, compute triads only for a random sample of *SampleEdges* edges, which is useful for approximate but quick computations.

Return value:

- int
    The number of edges that participate in at least one triad.

The following example shows how to calculate the number of edges in triads for nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet` (only shows first type)::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    NumTriadEdges = Graph.GetTriadEdges()
    print(NumTriadEdges)

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    NumTriadEdges = UGraph.GetTriadEdges()
    print(NumTriadEdges)

    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    NumTriadEdges = Network.GetTriadEdges()
    print(NumTriadEdges)
