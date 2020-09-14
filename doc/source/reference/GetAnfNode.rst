GetAnfNode
'''''''''''

.. function:: GetAnfNode(SrcNId, MxDist, IsDir, NApprox=32)

A graph method that returns approximate neighborhood sizes of a node. Prints the (approximate) number of nodes reachable from *SrcNId* in less than *MxDist* hops.

Parameters:

- *SrcNId*: int
    The node id for the starting node.

- *MxDist*: int
    Maximum number of hops the algorithm spreads from *SrcNId*.
    
- *IsDir*: bool
    Indicates whether the edges should be considered directed or undirected.

- (optional) *Napprox*: int
    Quality of approximation. See the ANF paper. Should be a multiple of 8.

Return value:

- :class:`TIntFltKdV`, a vector of (integer, float) pairs
    Each pair gives the distance H (in hops) and the number of nodes reachable in <= H hops.

The ANF paper: http://www.cs.cmu.edu/~christos/PUBLICATIONS/kdd02-anf.pdf


The following example shows how to use :func:`GetAnf` with
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.TNGraph, 100, 1000)
    SrcNId = 0
    DistNbrsV = Graph.GetAnfNode(SrcNId, 3, False, 32)
    for item in DistNbrsV:
        print(item.Dat())

    UGraph = snap.GenRndGnm(snap.TUNGraph, 100, 1000)
    SrcNId = 0
    DistNbrsV = UGraph.GetAnfNode(SrcNId, 3, False, 32)
    for item in DistNbrsV:
        print(item.Dat())

    Network = snap.GenRndGnm(snap.TNEANet, 100, 1000)
    SrcNId = 0
    DistNbrsV = Network.GetAnfNode(SrcNId, 3, False, 32)
    for item in DistNbrsV:
        print(item.Dat())
