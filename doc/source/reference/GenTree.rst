GenTree
'''''''''''''''
.. note::

    This page is a draft and under revision.


.. function:: GenTree(GraphType, Fanout, Levels, IsDir=True, ChildPointsToParent=True)

Generates a tree graph of *Levels* levels with every parent having Fanout children.

Parameters:

- *GraphType*: class (input)
    Type of gaph to create. :class:`PNGraph`, :class:`PUNGraph`, or :class:`PNEANet`

- *Fanout*: int (input)
    Number of children of each parent node

- *Levels*: int (input)
    Number of levels of the tree

- *IsDir*: bool (input)
    True for a directed graph, false for an undirected graph

- *ChildPointsToParent*: bool (input)
    True if children should point to their parents. Only applies to directed graphs.

Return Value:

- A new *PGraph*

The following examples shows how to generate a tree graph for networks of class :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    # A directed graph with 3 levels, fanout 3, and children pointing to their parents
    Graph = snap.GenTree(snap.PNGraph, 3, 3)
    for NI in Graph.Nodes():
      print "node: %d, out-degree %d, in-degree %d" % ( NI.GetId(), NI.GetOutDeg(), NI.GetInDeg())
    
    # An undirected graph with 3 levels and fanout 3
    Graph = snap.GenTree(snap.PUNGraph, 3, 3)
    for NI in Graph.Nodes():
      print "node: %d, out-degree %d, in-degree %d" % ( NI.GetId(), NI.GetOutDeg(), NI.GetInDeg())

    # A directed network with 3 levels, fanout 3, and children pointing to their parents
    Graph = snap.GenTree(snap.PNEANet, 3, 3)
    for NI in Graph.Nodes():
      print "node: %d, out-degree %d, in-degree %d" % ( NI.GetId(), NI.GetOutDeg(), NI.GetInDeg())

    