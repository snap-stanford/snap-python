GetSubTreeSz
''''''''''''


.. function:: GetSubTreeSz(Graph, StartNId, FollowOut, FollowIn)

Returns the BFS tree size (number of nodes) and depth (number of
levels) by following in-links and/or out-links of node *StartNId*.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

- *StartNId*: int (input)
    Starting node

- *FollowOut*: bool (input)
    Whether to follow out-links

- *FollowIn*: bool (input)
    Whether to follow in-links

Return value:

- tuple
    The tuple is of size 3 and consists of the number of nodes in the tree (twice), and the number of levels in the tree.

The following example shows how to get the size of the tree starting at node 0 with
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenTree(snap.PNGraph, 3, 3)
    results = snap.GetSubTreeSz(Graph, 0, True, False)
    print "Size %d, Depth %d" % (results[0], results[2])

    Graph = snap.GenTree(snap.PUNGraph, 3, 3)
    results = snap.GetSubTreeSz(Graph, 0, True, False)
    print "Size %d, Depth %d" % (results[0], results[2])

    Graph = snap.GenTree(snap.PNEANet, 3, 3)
    results = snap.GetSubTreeSz(Graph, 0, True, False)
    print "Size %d, Depth %d" % (results[0], results[2])