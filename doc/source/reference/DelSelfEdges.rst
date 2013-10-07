DelSelfEdges
''''''''''''

.. function:: DelSelfEdges (Graph)

Removes all the self-edges from the graph.

Parameters:

- *Graph*: the PGraph that will be modified by deleting self-edges

Return value:

- None


The following example shows how to delete self-edges in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

	#PNGraph Example
	Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
	Graph.AddEdge(1,1)
	for node in Graph.Nodes():
		for dest in node.GetOutEdges():
			if dest == node.GetId():
				print "Self edge on node " + str(node.GetId())

	snap.DelSelfEdges(Graph)
	print "Deleted self-edges"
	for node in Graph.Nodes():
		for dest in node.GetOutEdges():
			if dest == node.GetId():
				print "Self edge on node " + node.GetId()

	# PUNGraph Example
	Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
	Graph.AddEdge(1,1)
	for node in Graph.Nodes():
		for dest in node.GetOutEdges():
			if dest == node.GetId():
				print "Self edge on node " + str(node.GetId())

	snap.DelSelfEdges(Graph)
	print "Deleted self-edges"
	for node in Graph.Nodes():
		for dest in node.GetOutEdges():
			if dest == node.GetId():
				print "Self edge on node " + node.GetId()

	# PNEANet Example
	Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
	Graph.AddEdge(1,1)
	for node in Graph.Nodes():
		for dest in node.GetOutEdges():
			if dest == node.GetId():
				print "Self edge on node " + str(node.GetId())

	snap.DelSelfEdges(Graph)
	print "Deleted self-edges"
	for node in Graph.Nodes():
		for dest in node.GetOutEdges():
			if dest == node.GetId():
				print "Self edge on node " + node.GetId()