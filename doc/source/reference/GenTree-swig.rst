GenTree (SWIG)
''''''''''''''''

.. function:: GenTree(GraphType, Fanout, Levels, IsDir=True, ChildPointsToParent=True)

Generates a tree graph of *Levels* levels with every parent having *Fanout* children.

Parameters:

- *GraphType*: graph class (input)
    Class of output graph -- one of :class:`PNGraph`, :class:`PNEANet`, or :class:`PUNGraph`.

- *Fanout*: int (input)
    Number of children of each parent node.

- *Levels*: int (input)
    Number of levels of the tree.

- *IsDir*: bool (input)
    Indicates whether the edges should be directed or undirected. Defaults to directed. 

- *ChildPointsToParent*: bool (input)
    True if children should point to their parents. Only applies to directed graphs.

Return Value:

- graph
    A Snap.py graph of the specified type.


The following examples shows how to generate a tree graph for classes :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenTree(snap.PNGraph, 3, 3)
    for EI in Graph.Edges():
        print("edge: (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId()))
    
    UGraph = snap.GenTree(snap.PUNGraph, 3, 3)
    for EI in UGraph.Edges():
        print("edge: (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId()))

    Network = snap.GenTree(snap.PNEANet, 3, 3)
    for EI in Network.Edges():
        print("edge: (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId()))

    
