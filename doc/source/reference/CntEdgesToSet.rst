CntEdgesToSet
'''''''''''''

.. function:: CntEdgesToSet(NId, NodeSet)

A graph method that counts the number of edges between the given node with node id *NId* and the given set of nodes *NodeSet* in a graph. If the graph is a directed graph, this function will return edges occurring in both directions between the given *NId* and *NodeSet*.

Parameters:

- *NId*: int
	The node id of the source node.

- *NodeSet*: Python set() or :class:`TIntSet`, a set of ints
	The set of destination node ids.

Return Value:

- int
    The number of edges from node with id *NId* to nodes in the set *NodeSet*.


The following example shows how to use :func:`CntEdgesToSet` with :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    NodeSet = set()
    for NI in range(1,50):
        NodeSet.add(NI)
    NodeId = 65

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    EdgeCount = Graph.CntEdgesToSet(NodeId, NodeSet)
    print("Number of edges from %d to NodeSet in PNGraph = %d" % (NodeId, EdgeCount))

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    EdgeCount = UGraph.CntEdgesToSet(NodeId, NodeSet)
    print("Number of edges from %d to NodeSet in PUNGraph = %d" % (NodeId, EdgeCount))

    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    EdgeCount = Network.CntEdgesToSet(NodeId, NodeSet)
    print("Number of edges from %d to NodeSet in PNEANet = %d" % (NodeId, EdgeCount))
