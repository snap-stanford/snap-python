CntUniqUndirEdges
'''''''''''''''''
.. note::

    This page is a draft and under revision.


.. function:: CntUniqUndirEdges(Graph)

Counts unique undirected edges in the graph *Graph*. Nodes (u,v), where u!=v, are considered to be connected via an undirected edge if there exists an edge in either direction. 

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

Return value:

- int

The following example shows how to count unique undirected edges in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

		import snap

		Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
		print snap.CntUniqUndirEdges(Graph)

		Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
		print snap.CntUniqUndirEdges(Graph)

		Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
		print snap.CntUniqUndirEdges(Graph) 
