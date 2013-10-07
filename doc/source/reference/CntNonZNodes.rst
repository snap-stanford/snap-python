CntNonZNodes
'''''''''''

.. function:: CntNonZNodes(Graph)

Returns the number of nodes in *Graph* with degree greater than 0 (i.e., the number of nodes that are connected to other nodes). 

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

Return value:

- Integer, number of non-degree nodes

The following example shows how to obtain the number of nodes with a degree greater than 0 for nodes in :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

	import snap
	
	Graph = snap.GenRndGnm(snap.PNGraph, 100, 50)
	NonZeroNodes = snap.CntNonZNodes(Graph)
	print NonZeroNodes
			
	Graph = snap.GenRndGnm(snap.PUNGraph, 100, 50)
	NonZeroNodes = snap.CntNonZNodes(Graph)
	print NonZeroNodes
			
	Graph = snap.GenRndGnm(snap.PNEANet, 100, 50)
	NonZeroNodes = snap.CntNonZNodes(Graph)
	print NonZeroNodes
