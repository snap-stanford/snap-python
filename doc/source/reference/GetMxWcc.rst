GetMxWcc
'''''''''''

.. function:: PGraph GetMxWcc(Graph)

Get a graph representing the largest weakly connected component on an input ＊Graph＊.
A directed/undirected graph is connected if there exist an undirected path between any pair of nodes.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

Return value:

- *PGraph*: graph (output)
	A graph representing the largest weakly connected component on an input ＊Graph＊.

For more info see: http://en.wikipedia.org/wiki/Connected_component_(graph_theory)

The following example shows how to get a vector of bridge edges in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 500)
    PGraph = snap.GetMxWcc(Graph)
    
    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 500)
    PGraph = snap.GetMxWcc(Graph)

    Graph = snap.GenRndGnm(snap.PNEANet, 100, 500)
    PGraph = snap.GetMxWcc(Graph)
