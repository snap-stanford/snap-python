GetSubTreeSz
''''''''''''

.. function:: GetSubTreeSz(Graph, StartNId, FollowOut, FollowIn, TreeSz, TreeDepth)

Returns the BFS tree size (number of nodes) and depth (number of
levels) by following in-links (parameter FollowIn = true) and/or
out-links (parameter FollowOut = true) of node StartNId.

Parameters:

- *Graph*: graph (input)
    The desired degree sequence, sorted in descending order.

- *StartNId*: integer (input)
    Starting node

- *FollowOut*: boolean (input)
    Whether to follow out-links

- *FollowIn*: boolean (input)
    Whether to follow in-links

- *TreeSz*: integer (output)
    Number of nodes in the tree

- *TreeDepth*: integer (output)
    Number of levels in the tree

Return value:

- Number of nodes in the tree (same as TreeSz)

This function is not yet implemented, but it might work like this::

    import snap

    G = snap.TNGraph.New()
    for i in range(5):
    G.AddNode(i)
    G.AddEdge(0,1)
    G.AddEdge(0,2)
    G.AddEdge(2,3)
    G.AddEdge(2,4)

    TreeSz = snap.TInt()
    TreeDepth = snap.TInt()
    snap.GetSubTreeSz(G, 0, True, False, TreeSz, TreeDepth)
    print "Size %d, Depth %d" % (TreeSz, TreeDepth)
