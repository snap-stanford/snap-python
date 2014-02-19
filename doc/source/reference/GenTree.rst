GenTree
'''''''''

.. function:: GenTree(GraphType, Fanout, Levels, IsDir=True, ChildPointsToParent=True)

Generates a tree graph of *Levels* levels with every parent having *Fanout* children.

Parameters:

- *GraphType*: class (input)
    Type of graph to create. :class:`PNGraph`, :class:`PUNGraph`, or :class:`PNEANet`

- *Fanout*: int (input)
    Number of children of each parent node

- *Levels*: int (input)
    Number of levels of the tree

- *IsDir*: boolean (input)
    Indicates whether the edges should be directed or undirected. Defaults to directed. 

- *ChildPointsToParent*: bool (input)
    True if children should point to their parents. Only applies to directed graphs.

Return Value:

- graph
    A Snap.py graph of the specified type

The following examples shows how to generate a tree graph for classes :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    # A directed graph with 3 levels, fanout 3, and children pointing to their parents
    Graph = snap.GenTree(snap.PNGraph, 3, 3)
    for edge in Graph.Edges():
        print "%d, %d" % (edge.GetSrcNId(), edge.GetDstNId())
    
    # An undirected graph with 3 levels and fanout 3
    Graph = snap.GenTree(snap.PUNGraph, 3, 3)
    for edge in Graph.Edges():
        print "%d, %d" % (edge.GetSrcNId(), edge.GetDstNId())

    # A directed network with 3 levels, fanout 3, and children pointing to their parents
    Graph = snap.GenTree(snap.PNEANet, 3, 3)
    for edge in Graph.Edges():
        print "%d, %d" % (edge.GetSrcNId(), edge.GetDstNId())

    