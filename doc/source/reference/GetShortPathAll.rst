GetShortPathAll
'''''''''''''''

.. function:: GetShortPathAll(SrcNId, IsDir=false, MaxDist=TInt::Mx)

A graph method that returns the length of the shortest path from node SrcNId to all other nodes.

Parameters:

- *SrcNId*: int
    Node id for source node.

- (optional) *IsDir*: bool
    Indicates whether the edges should be considered directed or undirected.

- (optional) *MaxDist*: int
    Maximum number of hops that BFS expands to. This is helpful for speeding-up the code if one in interested only in nodes less than *MaxDist* away from *SrcNId*.

Return value:

- int
    The length of the shortest path from *SrcNId* to all other nodes.

- *NIdToDistH*: :class:`TIntH`, a hash table with integer keys and values
    Maps node id to shortest path distance. Only contains nodes that are reachable from *SrcNId*.


The following example shows how to calculate the length of the shortest path in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.TNGraph, 100, 1000)
    shortestPath, NIdToDistH = Graph.GetShortPathAll(10)
    for item in NIdToDistH:
        print(item, NIdToDistH[item])
    print(shortestPath)

    UGraph = snap.GenRndGnm(snap.TUNGraph, 100, 1000)
    shortestPath, NIdToDistH = UGraph.GetShortPathAll(10)
    for item in NIdToDistH:
        print(item, NIdToDistH[item])
    print(shortestPath)

    Network = snap.GenRndGnm(snap.TNEANet, 100, 1000)
    shortestPath, NIdToDistH = Network.GetShortPathAll(10)
    for item in NIdToDistH:
        print(item, NIdToDistH[item])
    print(shortestPath)

