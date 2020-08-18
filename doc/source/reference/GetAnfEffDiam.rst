GetAnfEffDiam
'''''''''''''

.. function:: GetAnfEffDiam(IsDir, Percentile, NApprox)

Returns a given *Percentile* of the shortest path length distribution of a *Graph* (based on a single run of ANF of approximation quality *NApprox*).

Parameters:

- *IsDir*: boolean
    Indicates whether the edges should be considered directed or undirected.

- *Percentile*: float
    Percentile of the shortest path length distribution of a Graph.

- *NApprox*: int
    Quality of approximation. Should be a multiple of 8.

Return value:

- float
    the given *Percentile* of the shortest path length distribution.

The following example shows how to use this function 
with graphs :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000) 
    Graph.GetAnfEffDiam(False, 0.9, 16)

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000) 
    UGraph.GetAnfEffDiam(False, 0.9, 16)
 
    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000) 
    Network.GetAnfEffDiam(False, 0.9, 16)
