CntEdgesToSet
'''''''''''''
.. note::

    This page is a draft and under revision.


.. function:: CntEdgesToSet(Graph, NId, NodeSet)

.. note::

    This function is not yet supported.

Counts the number of edges between the given node with node id *NId* and the given set of nodes *NodeSet* in the provided graph.

Parameters:

- *Graph*: graph (input)
	A Snap.py graph or network

- *NId*: int (input)
	The node id of the source node

- *NodeSet*: TIntSet, a set of ints (input)
	The set of destination node ids

Return Value:

- int

If Graph is a directed graph, this function will return edges occurring in both directions between the given NId and NodeSet.

The following example shows how to use :func:`CntEdgesToSet` with :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

	import snap

	NodeSet = snap.TIntSet()
	for Id in range(1,50):
		NodeSet.Add(Id)
	NodeId = 65

	Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
	EdgeCount = CntEdgesToSet(Graph, NodeId, NodeSet)
	print "Number of edges from %d to NodeSet in PNGraph = %d" % (NodeId, EdgeCount)

	UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
	EdgeCount = CntEdgesToSet(UGraph, NodeId, NodeSet)
	print "Number of edges from %d to NodeSet in PUNGraph = %d" % (NodeId, EdgeCount)

	NodeSet = snap.TIntSet()
	NodeSet.Add(1)
	NodeSet.Add(2)
	NodeSet.Add(3)
	NodeId = 4

	NGraph = snap.GenRndGnm(snap.PNEANet, 10, 50)
	EdgeCount = CntEdgesToSet(NGraph, NodeId, NodeSet)
	print "Number of edges from %d to NodeSet in PNEANet = %d" % (NodeId, EdgeCount)
