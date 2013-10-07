GetNodesAtHop
'''''''''''

.. function:: GetNodesAtHop(Graph, StartNId, Hop, NIdV, IsDir)

Finds IDs of all nodes that are at distance Hop from node StartNId.

Parameters:

- *PGraph*: graph (input)
    A Snap.py graph or a network

- *StartNId*: int (input)
    Starting node ID 
    PageRank scores. Keys are node IDs, values are computed PageRank scores.

- *Hop*: int (input)
    Integer specifying from how many hops away from the start node another node should
    be to be included in the return. 

- *NIdV*: TIntV (output)
    NIds of nodes Hop distance away from StartNId. Values are node ID ints.

- *IsDir*: bool (input)
    Boolean specifying whether the graph is directed. False: ignore edge directions and consider edges/paths as undirected (in case they are directed).

Return value:

- integer detailing how many nodes were found


The following example shows how to get a vector of nodes at hop distance
2 away from start node 1 using GetNodesAtHop for nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap
    from snap import *

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    NodeVec = snap.TIntV()
    GetNodesAtHop(Graph, 1, 2, NodeVec, True)
    for item in NodeVec:
        print item

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    NodeVec = snap.TIntV()
    GetNodesAtHop(Graph, 1, 2, NodeVec, True)
    for item in NodeVec:
        print item

    Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    NodeVec = snap.TIntV()
    GetNodesAtHop(Graph, 1, 2, NodeVec, True)
    for item in NodeVec:
        print item


