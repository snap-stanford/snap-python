GetSubTreeSz
''''''''''''

.. function:: GetSubTreeSz(StartNId, FollowOut, FollowIn)

A graph method that returns the BFS tree size (number of nodes) and depth (number of levels) by following in-links and/or out-links of node *StartNId*.

Parameters:

- *StartNId*: int
    Starting node id.

- *FollowOut*: bool
    Whether to follow out-links.

- *FollowIn*: bool
    Whether to follow in-links.

Return value:

- list: [int, int, int]
    The list is of size 3 and consists of the number of nodes in the tree (twice) and the number of levels in the tree.

The following example shows how to get the size of the tree starting at node 0 with
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenTree(snap.TNGraph, 3, 3)
    results = Graph.GetSubTreeSz(0, True, True)
    print("Size %d, Depth %d" % (results[0], results[2]))

    UGraph = snap.GenTree(snap.TUNGraph, 3, 3)
    results = UGraph.GetSubTreeSz(0, True, True)
    print("Size %d, Depth %d" % (results[0], results[2]))

    Network = snap.GenTree(snap.TNEANet, 3, 3)
    results = Network.GetSubTreeSz(0, True, True)
    print("Size %d, Depth %d" % (results[0], results[2]))
