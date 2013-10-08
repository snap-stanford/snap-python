GetRndESubGraph
'''''''''''''''
.. note::

    This page is a draft and under revision.


.. function:: GetRndESubGraph (Graph, NEdges)

Returns a random subgraph of graph Graph with NEdges edges.

Randomly selects NEdges edges from the input graph and returns a subgraph on those edges.

Parameters:

- *Graph* : graph (input)
	A Snap.py graph or a network

- *NEdges*: int (input)
	Number of desired edges to select for subgraph

Return value:

- graph
	Randomly generated subgraph with NEdges edges

.. note:: Does not error check to ensure that NEdges is non-negative and less than the total number of edges in the graph

Example::
	
	import snap
	Graph = snap.GenRndGraph()
	SubGraph = snap.GetRndESubGraph(Graph, Graph.GetEdges() / 2)
	for edge in SubGraph.Edges()
		print edge.GetSrcNId(), edge.GetDstNId()
