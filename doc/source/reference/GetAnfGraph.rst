GetAnfGraph
''''''

.. function::  GetAnfGraph(MxDist, IsDir, NApprox=32)

A graph method that calculates approximate neighborhoods. Returns the number of pairs of nodes reachable in less than or equal to H hops.

Parameters:

- *MxDist*: int
    Maximum number of hops the algorithm takes between pairs.

- *IsDir*: bool
    Indicates whether the edges should be considered directed or undirected.

- (optional) *NApprox*: int
    Quality of approximation. See the ANF paper (link below). Should be a multiple of 8.

Return value:

- :class:`TIntFltKd`, a vector of (int, float) pairs
    Each pair gives the distance H (in hops) and the number of nodes reachable in <= H hops.

The ANF paper: http://www.cs.cmu.edu/~christos/PUBLICATIONS/kdd02-anf.pdf


The following example shows how to use :func:`GetAnf` with
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.TNGraph, 100, 1000)
    DistNbrsV = Graph.GetAnfGraph(3, False, 32)
    for item in DistNbrsV:
        print(item.Dat())

    UGraph = snap.GenRndGnm(snap.TUNGraph, 100, 1000)
    DistNbrsV = UGraph.GetAnfGraph(3, False, 32)
    for item in DistNbrsV:
        print(item.Dat())

    Network = snap.GenRndGnm(snap.TNEANet, 100, 1000)
    DistNbrsV = Network.GetAnfGraph(3, False, 32)
    for item in DistNbrsV:
        print(item.Dat())
