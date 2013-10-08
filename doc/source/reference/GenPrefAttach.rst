GenPrefAttach
'''''''''''''
.. note::

    This page is a draft and under revision.


.. function:: GenPrefAttach(Nodes, NodesOutDeg, Rnd)

Generates a power-law degree distribution using Barabasi-Albert model of scale-free graphs.

Barabasi-Albert model of scale-free graphs. The graph has power-law degree distribution. See: Emergence of scaling in random networks by Barabasi and Albert. URL: http://arxiv.org/abs/cond-mat/9910332

Paramters: 

- *Nodes*: int (input)
	The number of nodes desired.

-*NodeOutDeg*: int (input)
	The out degree of each node desired. 

-*Rnd*: TRnd (input)
	a Random Generator 

Return Value: 
	
-PUNGraph
	An Undirected Graph representing the power-law degree distribution. 

Example::
	
	import snap 

	#Print all edges of graph created by GenPrefAttach()

	Rnd = snap.TRnd()
	graph = snap.GenPrefAttach(100, 10, Rnd)
	for node in graph.Nodes():
		for edge in node.GetOutEdges():
			print "Edge between %d and %d" % (node.GetId(), edge)
