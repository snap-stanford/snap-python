ConvertGraph
''''''''''''

.. function:: OutGraph ConvertGraph(POutGraph, InGraph, RenumberNodes = False)

Performs conversion of graph InGraph with an optional node renumbering.

Parameters:

- *POutGraph*: smart pointer to a graph type (input)
	A Snap.py smart pointer to a graph or network type, which determines the type of the output graph

- *InGraph*: graph (input)
	A Snap.py graph or network

- *RenumberNodes*: boolean (input)
	Determines whether the node IDs are preserved or not. If False, then nodes in the resulting graph have the same node IDs as nodes in InGraph. If True, then nodes in the resulting graph are renumbered sequentially from 0 to N-1. By default, the nodes are not renumbered.

Return Value:

- *OutGraph*: graph (output)
	A Snap.py graph or network, resulting from the conversion

Input and output graphs can have different types. Node and edge data is not copied, but it is shared by input and output graphs.

The following example shows how to convert :class:`TNGraph` to :class:`TUNGraph`, and :class:`TNEANet`::

	import snap

	Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
	UGraph = snap.ConvertGraph(snap.PUNGraph, Graph)
	for EI in UGraph.Edges():
		print "edge (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId())

	NGraph = snap.ConvertGraph(snap.PNEANet, Graph, True)
	for NI in NGraph.Nodes():
		print "node: %d, out-degree %d, in-degree %d" % (NI.GetId(), NI.GetOutDeg(), NI.GetInDeg())
