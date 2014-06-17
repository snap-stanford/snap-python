GetAnf
''''''

.. function::  GetAnf(Graph, DistNbrsV, MxDist, IsDir, NApprox=32)

Approximate Neighborhood Function of *Graph*. Returns the number of pairs of nodes reachable in less than or equal to H hops.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network.
    
- *DistNbrsV*: :class:`TIntFltKd`, a vector of (int, float) pairs (output)
    Maps between the distance H (in hops) and the number of nodes reachable in <= H hops.

- *MxDist*: int (input)
    Maximum number of hops the algorithm takes between pairs.

- *IsDir*: bool (input)
    Indicates whether the edges should be considered directed or undirected.

- *NApprox*: int (input)
    Quality of approximation. See the ANF paper (link below). Should be a multiple of 8.

Return value:

- None

The ANF paper: http://www.cs.cmu.edu/~christos/PUBLICATIONS/kdd02-anf.pdf


The following example shows how to use :func:`GetAnf` with
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    DistNbrsV = snap.TIntFltKdV()
    snap.GetAnf(Graph, DistNbrsV, 3, False, 32)
    for item in DistNbrsV:
        print item.Dat()

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    DistNbrsV = snap.TIntFltKdV()
    snap.GetAnf(UGraph, DistNbrsV, 3, False, 32)
    for item in DistNbrsV:
        print item.Dat()

    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    DistNbrsV = snap.TIntFltKdV()
    snap.GetAnf(Network, DistNbrsV, 3, False, 32)
    for item in DistNbrsV:
        print item.Dat()
