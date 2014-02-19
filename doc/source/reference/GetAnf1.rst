GetAnf
''''''

.. function::  GetAnf(Graph, DistNbrsV, MxDist, IsDir, NApprox=32)

Approximate Neighborhood Function of *Graph*. Returns the number of pairs of nodes reachable in less than or equal to H hops.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network
    
- *DistNbrsV*: TIntFltKd, a vector of (int, float) pairs (output)
    Maps between the distance H (in hops) and the number of nodes reachable in <= H hops

- *MxDist*: int (input)
    Maximum number of hops the algorithm takes between pairs

- *IsDir*: boolean (input)
    Indicates whether the edges should be considered directed or undirected.

- *NApprox*: int (input)
    Quality of approximation. See the ANF paper (link below)

Return value:

- None

The ANF paper: http://www.cs.cmu.edu/~christos/PUBLICATIONS/kdd02-anf.pdf

The following example shows how to use :func:`GetAnf` with
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    DistNbrsV = snap.TIntFltKdV()
    snap.GetAnf(Graph, DistNbrsV, 3, False)
    for item in DistNbrsV:
        print item.Dat()

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    DistNbrsV = snap.TIntFltKdV()
    snap.GetAnf(Graph, DistNbrsV, 3, False)
    for item in DistNbrsV:
        print item.Dat()

    Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    DistNbrsV = snap.TIntFltKdV()
    snap.GetAnf(Graph, DistNbrsV, 3, False)
    for item in DistNbrsV:
        print item.Dat()
