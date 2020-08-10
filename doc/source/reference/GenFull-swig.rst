GenFull (SWIG)
''''''''''''''

.. function:: GenFull(GraphType, Nodes)

Generates a complete graph on *Nodes* nodes. Graph has no self-loops.

Parameters:

- *GraphType*: graph class (input)
    Class of output graph -- one of :class:`PNGraph`, :class:`PNEANet`, or :class:`PUNGraph`.

- *Nodes*: int (input)
    The number of nodes used to generate the graph.

Return value:

- graph
    A Snap.py graph of the specified type.


The following example shows how to generate different types of fully connected graphs for classes :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenFull(snap.PNGraph, 5)
    for EI in Graph.Edges():
        print("edge: (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId()))

    UGraph = snap.GenFull(snap.PUNGraph, 5)
    for EI in UGraph.Edges():
        print("edge: (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId()))

    Network = snap.GenFull(snap.PNEANet, 5)
    for EI in Network.Edges():
        print("edge: (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId()))
