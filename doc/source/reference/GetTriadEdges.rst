GetTriadEdges
'''''''''''

.. function:: GetTriadEdges(Graph, SampleEdges = -1)

Counts the number of edges that participate in at least one triad.

Considers the graph as undirected.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

- *SampleEdges*: If SampleEdges != -1, then compute triads only for a random sample of SampleEdges edges. Useful for approximate but quick computations.

Return value:

- int

The following example shows how to calculate the number of edges in triads for nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`:: (only shows first type):

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)

    NumTriadEdges = snap.GetTriadEdges(Graph)

    # Sample 1/10, multiply by 10 to approximate
    AppxNumTriadEdges = snap.GetTriadEdges(Graph, 100) * 10
