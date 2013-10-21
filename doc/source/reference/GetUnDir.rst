GetUnDir
''''''''


.. function:: GetUnDir(Graph)

Returns an undirected version of the graph. For every edge (u,v) an edge (v,u) is added (if it does not yet exist).

Parameters:

- *Graph*: directed graph (input)
    A Snap.py graph or a network

Return value:

- graph
    The un-directed version of graph *Graph*. If *Graph* is undirected, returns an identical graph.  

The following example shows how to convert directed graph to un-directed graph using
:class:`TNGraph`::

	import snap

	G1 = snap.TNGraph.New()
	G1.AddNode(1)
	G1.AddNode(3)
	G1.AddNode(5)

	G1.AddEdge(1,3)
	G1.AddEdge(3,5)
	G1.AddEdge(1,5)

	UG = snap.GetUnDir(G1)

	for EI in UG.Edges():
		print "edge (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId())