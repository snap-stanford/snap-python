CntEdgesToSet (SWIG)
''''''''''''''''''''

.. function:: CntEdgesToSet(Graph, NId, NodeSet)

Counts the number of edges between the given node with node id *NId* and the given set of nodes *NodeSet* in the provided graph *Graph*. If *Graph* is a directed graph, this function will return edges occurring in both directions between the given *NId* and *NodeSet*.

Parameters:

- *Graph*: graph (input)
	A Snap.py graph or network.

- *NId*: int (input)
	The node id of the source node.

- *NodeSet*: :class:`TIntSet`, a set of ints (input)
	The set of destination node ids.

Return Value:

- int
    The number of edges from node with id *NId* to nodes in the set *NodeSet*.


The following example shows how to use :func:`CntEdgesToSet` with :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

	import snap

    NodeSet = snap.TIntSet()
    for NI in range(1,50):
        NodeSet.AddKey(NI)
    NodeId = 65

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    EdgeCount = snap.CntEdgesToSet(Graph, NodeId, NodeSet)
    print("Number of edges from %d to NodeSet in PNGraph = %d" % (NodeId, EdgeCount))

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    EdgeCount = CntEdgesToSet(UGraph, NodeId, NodeSet)
    print("Number of edges from %d to NodeSet in PUNGraph = %d" % (NodeId, EdgeCount))

    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    EdgeCount = CntEdgesToSet(Network, NodeId, NodeSet)
    print("Number of edges from %d to NodeSet in PNEANet = %d" % (NodeId, EdgeCount))
