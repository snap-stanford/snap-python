GetBetweennessCentr
'''''''''''''''''''

.. function:: GetBetweennessCentr(NodeFrac=1.0, IsDir=False)

A graph method that computes (approximate) Node and Edge Betweenness Centrality based on a sample of *NodeFrac* nodes.

Parameters:

- (optional) *NodeFrac*: float
    Quality of the approximation. NodeFrac=1.0 gives exact betweenness values.

- (optional) *IsDir*: bool
    Indicates whether the edges should be considered directed (*True*) or undirected (*False*).

Return Value:

- *NIdBtwH*: :class:`TIntFltH`, a hash table with int keys and float values
    Hash table mapping node ids to their corresponding betweenness centrality values.

- *EdgeBtwH*: :class:`TIntPrFltH`, a hash table with int pair keys and float values
    Hash table mapping edges (provided as pairs of node ids) to their corresponding betweenness centrality values.

See "A Faster Algorithm for Betweenness Centrality", Ulrik Brandes, Journal of Mathematical Sociology, 2001, and "Centrality Estimation in Large Networks", Urlik Brandes and Christian Pich, 2006 for more details. 


The following example shows how to calculate Betweenness Centrality scores for nodes and edges in
:class:`TNGraph`,
:class:`TUNGraph`, and
:class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.TNGraph, 100, 1000)
    Nodes, Edges = Graph.GetBetweennessCentr(1.0)
    for node in Nodes:
        print("node: %d centrality: %f" % (node, Nodes[node]))
    for edge in Edges:
        print("edge: (%d, %d) centrality: %f" % (edge.GetVal1(), edge.GetVal2(), Edges[edge]))

    UGraph = snap.GenRndGnm(snap.TUNGraph, 100, 1000)
    Nodes, Edges = UGraph.GetBetweennessCentr(1.0)
    for node in Nodes:
        print("node: %d centrality: %f" % (node, Nodes[node]))
    for edge in Edges:
        print("edge: (%d, %d) centrality: %f" % (edge.GetVal1(), edge.GetVal2(), Edges[edge]))

    Network = snap.GenRndGnm(snap.TNEANet, 100, 1000)
    Nodes, Edges = Network.GetBetweennessCentr(1.0)
    for node in Nodes:
        print("node: %d centrality: %f" % (node, Nodes[node]))
    for edge in Edges:
        print("edge: (%d, %d) centrality: %f" % (edge.GetVal1(), edge.GetVal2(), Edges[edge]))

