GetBfsTree (SWIG)
''''''''''''''''''

.. function:: GetBfsTree(Graph, StartNId, FollowOut, FollowIn)

Returns a directed Breadth-First-Search tree rooted at *StartNId*. The nodes in the tree correspond to those of *Graph*, and the edges represent the edges traversed by the breadth-first search on *Graph* starting from *StartNId*. The tree is created by traversing along out-links (parameter *FollowOut* = True) and/or in-links (parameter *FollowIn* = True). 

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network.

- *StartNId*: int (input)
    Id of the root node of the Breadth-First-Search tree.

- *FollowOut*: bool (input)
    A bool specifying if the graph should be constructed by following the outward links.

- *FollowIn*: bool (input)
    A bool specifying if the graph should be constructed by following inward links.

Return value:

- directed graph
    A Snap.py directed graph whose nodes correspond to those of the original graph and whose edges represent the edges traversed by the breadth-first search.


The following examples show how to use :func:`GetBfsTree` with graphs of type
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    BfsTree = snap.GetBfsTree(Graph, 1, True, False)
    for EI in BfsTree.Edges():
        print("Edge from %d to %d in generated tree." % (EI.GetSrcNId(), EI.GetDstNId()))

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    BfsTree = snap.GetBfsTree(UGraph, 1, True, False)
    for EI in BfsTree.Edges():
        print("Edge from %d to %d in generated tree." % (EI.GetSrcNId(), EI.GetDstNId()))

    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    BfsTree = snap.GetBfsTree(Network, 1, True, False)
    for EI in BfsTree.Edges():
        print("Edge from %d to %d in generated tree." % (EI.GetSrcNId(), EI.GetDstNId()))
