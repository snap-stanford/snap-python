GetUnDir
''''''''
.. note::

    This page is a draft and under revision.


.. function:: GetUnDir(Graph)

Returs an undirected version of the graph. For every edge (u,v) an edge (v,u) is added (if it does not yet exist).

Parameters:

- *Graph*: directed graph (input)
    A Snap.py directed graph

Return value:

- *Graph*: un-directed graph 

The following example shows how to convert directed graph to un-directed graph for 
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

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