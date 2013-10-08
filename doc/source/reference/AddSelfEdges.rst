AddSelfEdges
''''''''''''

.. function:: AddSelfEdges(Graph)

Adds a self-edge to every node in the *Graph*.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

Return value:

- None

The following example shows how to use AddSelfEdges on
:class:`PNGraph`, :class:`PUNGraph`, and :class:`PNEANet`::

	from snap import *

	### PNGraph
	print "--- PNGraph ---"
	Graph = GenRndGnm(PNGraph, 100, 1000)

	# Print starting number of edges and count number of self edges
	print Graph.GetEdges(), "starting total edges"
	nSelfEdges = 0
	for NI in Graph.Nodes():
	    if Graph.IsEdge(NI.GetId(),NI.GetId()): nSelfEdges += 1
	print nSelfEdges, "starting self edges"

	# Add Self Edges
	AddSelfEdges(Graph)
	print Graph.GetEdges(), "ending total edges"
	nSelfEdges = 0
	for NI in Graph.Nodes():
	    if Graph.IsEdge(NI.GetId(),NI.GetId()): nSelfEdges += 1
	print nSelfEdges, "ending self edges"




	### PUNGraph
	print "--- PUNGraph ---"
	Graph = GenRndGnm(PUNGraph, 100, 1000)
	
	# Print starting number of edges and count number of self edges
	print Graph.GetEdges(), "starting total edges"
	nSelfEdges = 0
	for NI in Graph.Nodes():
	    if Graph.IsEdge(NI.GetId(),NI.GetId()): nSelfEdges += 1
	print nSelfEdges, "starting self edges"
	
	# Add Self Edges
	AddSelfEdges(Graph)
	print Graph.GetEdges(), "ending total edges"
	nSelfEdges = 0
	for NI in Graph.Nodes():
	    if Graph.IsEdge(NI.GetId(),NI.GetId()): nSelfEdges += 1
	print nSelfEdges, "ending self edges"




	### PNEANet
	print "--- PNEANet ---"
	Graph = GenRndGnm(PNEANet, 100, 1000)
	
	# Print starting number of edges and count number of self edges
	print Graph.GetEdges(), "starting total edges"
	nSelfEdges = 0
	for NI in Graph.Nodes():
	    if Graph.IsEdge(NI.GetId(),NI.GetId()): nSelfEdges += 1
	print nSelfEdges, "starting self edges"
	
	# Add Self Edges
	AddSelfEdges(Graph)
	print Graph.GetEdges(), "ending total edges"
	nSelfEdges = 0
	for NI in Graph.Nodes():
	    if Graph.IsEdge(NI.GetId(),NI.GetId()): nSelfEdges += 1
	print nSelfEdges, "ending self edges"
