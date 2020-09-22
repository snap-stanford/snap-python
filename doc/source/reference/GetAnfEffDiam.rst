GetAnfEffDiam
'''''''''''''

.. function:: GetAnfEffDiam(IsDir, Percentile, NApprox)

A graph method that returns a given *Percentile* of the shortest path length distribution (based on a single run of ANF of approximation quality *NApprox*).

Parameters:

- *IsDir*: boolean
    Indicates whether the edges should be considered directed or undirected.

- *Percentile*: float
    Percentile of the shortest path length distribution.

- *NApprox*: int
    Quality of approximation. Should be a multiple of 8.

Return value:

- float
    the given *Percentile* of the shortest path length distribution.

The following example shows how to use this function 
with :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.TNGraph, 100, 1000) 
    print(Graph.GetAnfEffDiam(False, 0.9, 16))

    UGraph = snap.GenRndGnm(snap.TUNGraph, 100, 1000) 
    print(UGraph.GetAnfEffDiam(False, 0.9, 16))
 
    Network = snap.GenRndGnm(snap.TNEANet, 100, 1000) 
    print(Network.GetAnfEffDiam(False, 0.9, 16))
