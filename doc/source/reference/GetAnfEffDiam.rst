GetAnfEffDiam
'''''''''''''

.. function:: GetAnfEffDiam(Graph, IsDir, Percentile, NApprox)

Returns a given *Percentile* of the shortest path length distribution of a *Graph* (based on a single run of ANF of approximation quality *NApprox*).

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network.

- *IsDir*: boolean (input)
    Indicates whether the edges should be considered directed or undirected.

- *Percentile*: float (input)
    Percentile of the shortest path length distribution of a Graph.

- *NApprox*: int (input)
    Quality of approximation. Should be a multiple of 8.

Return value:

- float
    the given *Percentile* of the shortest path length distribution.

The following example shows how to use this function 
with graphs :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

	Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000) 
	snap.GetAnfEffDiam(Graph, False, 0.9, 16)

	UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000) 
	snap.GetAnfEffDiam(UGraph, False, 0.9, 16)
	
	Network = snap.GenRndGnm(snap.PNEANet, 100, 1000) 
	snap.GetAnfEffDiam(Network, False, 0.9, 16)
