GetTriadEdges
'''''''''''''

.. function:: GetTriadEdges(Graph, SampleEdges=-1)

Counts the number of edges that participate in at least one triad. Considers the graph as undirected.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

- *SampleEdges*: int (input)
    If SampleEdges != -1, then compute triads only for a random sample of SampleEdges edges. Useful for approximate but quick computations.

Return value:

- int
    The number of edges that participate in at least one triad.

The following example shows how to calculate the number of edges in triads for nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`:: (only shows first type)::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    NumTriadEdges = snap.GetTriadEdges(Graph)
    print NumTriadEdges

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    NumTriadEdges = snap.GetTriadEdges(Graph)
    print NumTriadEdges

    Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    NumTriadEdges = snap.GetTriadEdges(Graph)
    print NumTriadEdges