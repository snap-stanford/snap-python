GetAnf (SWIG)
''''''''''''''''''

.. function:: GetAnf(Graph, SrcNId, DistNbrsV, MxDist, IsDir, NApprox=32)
   :noindex:

Approximate neighborhood function of a node. Prints the (approximate) number of nodes reachable from *SrcNId* in less than *MxDist* hops.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network.

- *SrcNId*: int (input)
    The node id for the starting node.
    
- *DistNbrsV*: :class:`TIntFltKdV`, a vector of (integer, float) pairs (output)
    Maps between the distance H (in hops) and the number of nodes reachable in <= H hops.

- *MxDist*: int (input)
    Maximum number of hops the algorithm spreads from *SrcNId*.
    
- *IsDir*: bool (input)
    Indicates whether the edges should be considered directed or undirected.

- *Napprox*: int (input)
    Quality of approximation. See the ANF paper. Should be a multiple of 8.

Return value:

- None

The ANF paper: http://www.cs.cmu.edu/~christos/PUBLICATIONS/kdd02-anf.pdf


The following example shows how to use :func:`GetAnf` with
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    SrcNId = 0
    DistNbrsV = snap.TIntFltKdV()
    snap.GetAnf(Graph, SrcNId, DistNbrsV, 3, False, 32)
    for item in DistNbrsV:
        print(item.Dat())

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    SrcNId = 0
    DistNbrsV = snap.TIntFltKdV()
    snap.GetAnf(UGraph, SrcNId, DistNbrsV, 3, False, 32)
    for item in DistNbrsV:
        print(item.Dat())

    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    SrcNId = 0
    DistNbrsV = snap.TIntFltKdV()
    snap.GetAnf(Network, SrcNId, DistNbrsV, 3, False, 32)
    for item in DistNbrsV:
        print(item.Dat())
