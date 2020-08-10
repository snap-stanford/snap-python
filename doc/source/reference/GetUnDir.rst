GetUnDir
''''''''

.. function:: GetUnDir()

A graph method that returns a new graph which is an undirected version of the graph. For every edge (u,v) an edge (v,u) is added (if it does not yet exist).

Parameters:

- None

Return value:

- graph
    The undirected version of the graph. If the graph is undirected, returns an identical graph.  

The following example shows how to convert directed graph to undirected graph using
:class:`TNGraph`::

	import snap

	Graph = snap.TNGraph.New()
	Graph.AddNode(1)
	Graph.AddNode(3)
	Graph.AddNode(5)
	Graph.AddEdge(1,3)
	Graph.AddEdge(3,5)
	Graph.AddEdge(1,5)

	UGraph = Graph.GetUnDir()
	for EI in UGraph.Edges():
		print("edge (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId()))
