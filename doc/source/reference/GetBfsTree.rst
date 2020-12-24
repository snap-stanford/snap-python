GetBfsTree
''''''''''

.. function:: GetBfsTree(StartNId, FollowOut, FollowIn)

A graph method that returns a directed Breadth-First-Search tree rooted at *StartNId*. The nodes in the tree correspond to those of the graph, and the edges represent the edges traversed by the breadth-first search on the graph starting from *StartNId*. The tree is created by traversing along out-links (parameter *FollowOut* = True) and/or in-links (parameter *FollowIn* = True). 

Parameters:

- *StartNId*: int
    Id of the root node of the Breadth-First-Search tree.

- *FollowOut*: bool
    A bool specifying if the graph should be constructed by following the outward links.

- *FollowIn*: bool
    A bool specifying if the graph should be constructed by following inward links.

Return value:

- directed graph
    A directed graph whose nodes correspond to those of the original graph and whose edges represent the edges traversed by the breadth-first search.


The following examples show how to use :func:`GetBfsTree` with graphs of type
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.TNGraph, 100, 1000)
    BfsTree = Graph.GetBfsTree(1, True, False)
    for EI in BfsTree.Edges():
        print("Edge from %d to %d in generated tree." % (EI.GetSrcNId(), EI.GetDstNId()))

    UGraph = snap.GenRndGnm(snap.TUNGraph, 100, 1000)
    BfsTree = UGraph.GetBfsTree(1, True, False)
    for EI in BfsTree.Edges():
        print("Edge from %d to %d in generated tree." % (EI.GetSrcNId(), EI.GetDstNId()))

    Network = snap.GenRndGnm(snap.TNEANet, 100, 1000)
    BfsTree = Network.GetBfsTree(1, True, False)
    for EI in BfsTree.Edges():
        print("Edge from %d to %d in generated tree." % (EI.GetSrcNId(), EI.GetDstNId()))
