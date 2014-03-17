GetShortPath
''''''''''''

.. function:: GetShortPath(Graph, SrcNId, NIdToDistH, IsDir=false, MaxDist=TInt::Mx)

Returns the length of the shortest path from node SrcNId to all other nodes in the network.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network.

- *SrcNId*: int (input)
    Node id for source node.

- *NIdToDistH*: :class:`TIntH`, a hash table with integer keys and values (output)
    Maps node id to shortest path distance. Only contains nodes that are reachable from *SrcNId*.

- *IsDir*: bool (input)
    Indicates whether the edges should be considered directed or undirected.

- *MaxDist*: int (input)
    Maximum number of hops that BFS expands to. This is helpful for speeding-up the code if one in interested only in nodes less than *MaxDist* away from *SrcNId*.

Return value:

- int
    The length of the shortest path from *SrcNId* to all other nodes.


The following example shows how to calculate the length of the shortest path in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    NIdToDistH = snap.TIntH()
    shortestPath = snap.GetShortPath(Graph, 10, NIdToDistH)
    for item in NIdToDistH:
        print item, NIdToDistH[item]
    print shortestPath

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    NIdToDistH = snap.TIntH()
    shortestPath = snap.GetShortPath(UGraph, 10, NIdToDistH)
    for item in NIdToDistH:
        print item, NIdToDistH[item]
    print shortestPath

    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    NIdToDistH = snap.TIntH()
    shortestPath = snap.GetShortPath(Network, 10, NIdToDistH)
    for item in NIdToDistH:
        print item, NIdToDistH[item]
    print shortestPath

