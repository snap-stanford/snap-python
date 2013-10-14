GetShortPath
''''''''''''
.. note::

    This page is a draft and under revision.


.. function:: GetShortPath(Graph, SrcNId, NIdToDistH, IsDir=false, MaxDist=TInt::Mx)

Returns the length of the shortest path from node SrcNId to all other nodes in the network.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

- *SrcNId*: integer (input)
    ID of the Source node.

- *NIdToDistH*: hash table with integer keys and values (output)
    Maps node ID to shortest path distance. Only contains nodes that are reachable from SrcNId.

- *IsDir*: boolean (input)
    False: ignore edge directions and consider edges/paths as undirected (in case they are directed).

- *MaxDist*: integer (input)
    Maximum number of hops that BFS expands to. This is helpful for speeding-up the code if one in interested only in nodes less than MaxDist away from SrcNId.

Return value:

- Integer value. Length of the shortest path from SrcNId to all other nodes.

The following example shows how to calculate the length of the shortest path in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    NIdToDistH = snap.TIntH()
    shortestPath = snap.GetShortPath(Graph,10, NIdToDistH)
    for item in NIdToDistH:
        print item.GetKey(), item.GetDat()
    print shortestPath

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    NIdToDistH = snap.TIntH()
    shortestPath = snap.GetShortPath(Graph,10, NIdToDistH)
    for item in NIdToDistH:
        print item.GetKey(), item.GetDat()
    print shortestPath

    Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    NIdToDistH = snap.TIntH()
    shortestPath = snap.GetShortPath(Graph,10, NIdToDistH)
    for item in NIdToDistH:
        print item.GetKey(), item.GetDat()
    print shortestPath

