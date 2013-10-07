DelZeroDegNodes 
'''''''''''''''

.. function:: DelZeroDegNodes(Graph)

Removes all the zero-degree nodes, that isolated nodes, from the graph.

Parameters:

- *Graph*: graph (input and output)
    A Snap.py graph

Return value:

- None

The following example shows how to delete all zero-degree nodes for 
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

	import snap
	
	G1 = snap.TNGraph.New()
	G1.AddNode(1)
	G1.AddNode(2)
	G1.AddNode(3)
	G1.AddNode(4)
	G1.AddNode(5)
	
	G1.AddEdge(1,3)
	G1.AddEdge(3,5)
	G1.AddEdge(1,5)
	
	for NI in G1.Nodes():
		print "node: %d, out-degree %d, in-degree %d" % ( NI.GetId(), NI.GetOutDeg(), NI.GetInDeg())
	
	snap.DelZeroDegNodes(G1)
	
	for NI in G1.Nodes():
	 print "node: %d, out-degree %d, in-degree %d" % ( NI.GetId(), NI.GetOutDeg(), NI.GetInDeg())
	 
	 
	
	 G1 = snap.TUNGraph.New()
	 G1.AddNode(1)
	 G1.AddNode(2)
	 G1.AddNode(3)
	 G1.AddNode(4)
	 G1.AddNode(5)
	 
	 G1.AddEdge(1,3)
	 G1.AddEdge(3,5)
	 G1.AddEdge(1,5)
	 
	 for NI in G1.Nodes():
	 	print "node: %d, out-degree %d, in-degree %d" % ( NI.GetId(), NI.GetOutDeg(), NI.GetInDeg())
	 
	 snap.DelZeroDegNodes(G1)
	 
	 for NI in G1.Nodes():
	 print "node: %d, out-degree %d, in-degree %d" % ( NI.GetId(), NI.GetOutDeg(), NI.GetInDeg())
	 
	 G1 = snap.TNEANet.New()
	 G1.AddNode(1)
	 G1.AddNode(2)
	 G1.AddNode(3)
	 G1.AddNode(4)
	 G1.AddNode(5)
	 
	 G1.AddEdge(1,3)
	 G1.AddEdge(3,5)
	 G1.AddEdge(1,5)
	 
	 for NI in G1.Nodes():
	 	print "node: %d, out-degree %d, in-degree %d" % ( NI.GetId(), NI.GetOutDeg(), NI.GetInDeg())
	 
	 snap.DelZeroDegNodes(G1)
	 
	 for NI in G1.Nodes():
	 	print "node: %d, out-degree %d, in-degree %d" % ( NI.GetId(), NI.GetOutDeg(), NI.GetInDeg())
	 
	 