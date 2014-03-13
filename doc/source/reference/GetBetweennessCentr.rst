GetBetweennessCentr
'''''''''''''''''''

.. function:: GetBetweennessCentr(Graph, NIdBtwH, EdgeBtwH, NodeFrac=1.0)

Computes (approximate) Node and Edge Betweenness Centrality based on a sample of *NodeFrac* nodes. See "A Faster Algorithm for Betweenness Centrality", Ulrik Brandes, Journal of Mathematical Sociology, 2001, and "Centrality Estimation in Large Networks", Urlik Brandes and Christian Pich, 2006 for more details. 

Parameters:

- *Graph*: undirected graph (input)
    A Snap.py undirected graph.

- *NIdBtwH*: TIntFltH, a hash table with int keys and float values (output)
    Hash table mapping node ids to their corresponding betweenness centrality values.

- *EdgeBtwH*: TIntPrFltH, a hash table with int pair keys and float values (output)
    Hash table mapping edges (provided as pairs of node ids) to their corresponding betweenness centrality values.

- *NodeFrac*: float (input)
    Quality of the approximation. NodeFrac=1.0 gives exact betweenness values.


The following example shows how to calculate Betweenness Centrality scores for nodes and edges in
:class:`TUNGraph`::

    import snap

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    Nodes = snap.TIntFltH()
    Edges = snap.TIntPrFltH()
    snap.GetBetweennessCentr(UGraph, Nodes, Edges, 1.0)

    for node in Nodes:
        print "node: %d centrality: %f" % (node, Nodes[node])

    for edge in Edges:
        print "edge: (%d, %d) centrality: %f" % (edge.GetVal1(), edge.GetVal2(), Edges[edge])
