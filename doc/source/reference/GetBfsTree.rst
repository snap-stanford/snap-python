GetBfsTree
'''''''''''''''


Function Definition

.. function:: GetBfsTree:: GetBfsTree(Graph, StartNId, FollowOut, FollowIn)

Returns a directed Breadth-First-Search tree rooted at *StartNId*. The nodes in the tree correspond to those of *Graph*, and the edges represent the edges traversed by the breadth-first search on *Graph* starting from *StartNId*. The tree is created by traversing along out-links (parameter *FollowOut* = true) and/or in-links (parameter *FollowIn* = true). 


Parameters:

- *Graph*
    A Snap.py graph or a network

- *StartNId*
    Id of the root node of the BST

- *FollowOut*
    Boolean suggesting if the graph should be constructed by following the outward links.

- *FollowIn*
    Boolean suggesting if the graph should be constructed by following inward links.


Return value:

- PNGraph:
    Graph whose nodes correspond to those of the original graph and whose edges represent the edges traversed by the breadth-first search.

The following examples show how to use :func:`GetBfsTree` with graphs of type
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    BfsTree = snap.GetBfsTree(Graph, 1, True, False)
    for EI in BfsTree.Edges():
        print "Edge from %d to %d in generated tree." % (EI.GetSrcNId(), EI.GetDstNId())

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    BfsTree = snap.GetBfsTree(Graph, 1, True, False)
    for EI in BfsTree.Edges():
        print "Edge from %d to %d in generated tree." % (EI.GetSrcNId(), EI.GetDstNId())

    Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    BfsTree = snap.GetBfsTree(Graph, 1, True, False)
    for EI in BfsTree.Edges():
        print "Edge from %d to %d in generated tree." % (EI.GetSrcNId(), EI.GetDstNId())