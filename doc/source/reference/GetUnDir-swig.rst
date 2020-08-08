GetUnDir (SWIG)
'''''''''''''''

.. function:: GetUnDir(Graph)

Returns an undirected version of the graph. For every edge (u,v) an edge (v,u) is added (if it does not yet exist).

Parameters:

- *Graph*: directed graph (input)
    A Snap.py graph or a network.

Return value:

- graph
    The un-directed version of graph *Graph*. If *Graph* is undirected, returns an identical graph.  

The following example shows how to convert directed graph to un-directed graph using
:class:`TNGraph`::

	import snap

	Graph = snap.TNGraph.New()
	Graph.AddNode(1)
	Graph.AddNode(3)
	Graph.AddNode(5)
	Graph.AddEdge(1,3)
	Graph.AddEdge(3,5)
	Graph.AddEdge(1,5)

	UGraph = snap.GetUnDir(Graph)
	for EI in UGraph.Edges():
		print("edge (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId()))
