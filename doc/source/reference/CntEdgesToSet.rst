CntEdgesToSet
'''''''''''''

.. function:: int CntEdgesToSet(Graph, NId, NodeSet)

.. note::

    This functions is not yet supported.

Counts the number of edges between the given node and the given set of nodes in the provided graph.

Parameters:

- *Graph*: graph (input)
	A Snap.py graph or network

- *NId*: int (input)
	The node id of the source node

- *NodeSet*: TIntSet (input)
	The set of destination node ids

Return Value:

- *EdgeCount*: int (output)
	The number of edges between the node NId and the nodes in NodeSet

If Graph is a directed graph, this function will return edges occurring in both directions between the given NId and NodeSet.

The following example shows how to count edges to a node set in :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

	import snap

	Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
	NodeSet = snap.TIntSet()
	for Id in range(1,50):
		NodeSet.Add(Id)
	NodeId = 65
	EdgeCount = CntEdgesToSet(Graph, NodeId, NodeSet)
	print "Number of edges from %d to NodeSet in PNGraph = %d" % (NodeId, EdgeCount)

	UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
	EdgeCount = CntEdgesToSet(UGraph, NodeId, NodeSet)
	print "Number of edges from %d to NodeSet in PUNGraph = %d" % (NodeId, EdgeCount)

	NGraph = snap.GenRndGnm(snap.PNEANet, 10, 50)
	NodeSet = snap.TIntSet()
	NodeSet.Add(1)
	NodeSet.Add(2)
	NodeSet.Add(3)
	NodeId = 4
	EdgeCount = CntEdgesToSet(NGraph, NodeId, NodeSet)
	print "Number of edges from %d to NodeSet in PNEANet = %d" % (NodeId, EdgeCount)
