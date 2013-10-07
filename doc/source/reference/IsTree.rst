IsTree (Graph)
''''''''''''''''''''''''''''''''''''''''''

.. function:: bool IsTree(Graph)

Determines if the graph is a connected tree.  As a special case, if a graph has one node and no edges, it is a tree.  If there are any orphaned nodes, the graph is not a tree.

Parameters:

- *Graph*: (input) A Snap.py graph or a network

Return value: 

- bool: true if this graph represents a tree and false otherwise

The following example shows how to detect trees in 
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

	g = snap.TNGraph.New()

	g.AddNode(1)
	g.AddNode(2)
	g.AddEdge(1,2)
	g.AddNode(3)
	g.AddEdge(1,3)

	print snap.IsTree(g)  # 'false'

	g.AddNode(4)
	g.AddEdge(4,1)

	print snap.IsTree(g) # 'false'

	ug = snap.ConvertGraph(snap.PUNGraph, g)
	print snap.IsTree(ug) # 'true'

	net = snap.ConvertGraph(snap.PNEANet, g)
	print snap.IsTree(net) # 'false'
