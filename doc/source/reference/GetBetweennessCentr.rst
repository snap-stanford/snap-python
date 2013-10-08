GetBetweennessCentr
'''''''''''''''''''

.. function:: GetBetweennessCentr(Graph, NIdBtwH, EdgeBtwH, NodeFrac=1.0)

.. note::

    This functions is not yet supported.

Computes (approximate) Node and Edge Betweenness Centrality based on a sample o NodeFrac nodes. See "A Faster Algorithm for Betweenness Centrality", Ulrik Brandes, Journal of Mathematical Sociology, 2001, and "Centrality Estimation in Large Networks", Urlik Brandes and Christian Pich, 2006 for more details. 

Parameters:

- *Graph*: PUNGraph graph (input)
    An undirected Snap.py graph or a network

- *NIdBtwH*: hash table of int keys and float values (output)
    Hash table mapping node ids to their corresponding betweenness centrality values.

- *EdgeBtwH*: hash table of int pair keys and float values (output)
    Hash table mapping edges (provided as pairs of node ids) to their corresponding betweenness centrality values.

- *NodeFrac*: float (input)
    Quality of the approximation. NodeFrac=1.0 gives exact betweenness values.

For more info see: http://en.wikipedia.org/wiki/Betweenness_centrality

The following example shows how to calculate Betweenness Centrality scores for nodes and edges in
:class:`TUNGraph`::

    import snap

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    Nodes = snap.TIntFltH()
    Edges = snap.TIntPrFltH()
    snap.GetBetweennessCentr(Graph, Nodes, Edges, 1.0)

    for node in Nodes:
      print node.GetKey(), node.GetDat()

    for edge in Edges:
      pair = edge.GetKey()
      print pair.GetVal1(), '->', pair.GetVal2(), edge.GetDat()
