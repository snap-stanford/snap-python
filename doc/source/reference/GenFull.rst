GenFull
'''''''

.. function:: GenFull(GraphType, Nodes)

Generates a complete graph on Nodes nodes. Graph has no self-loops.

Parameters:

- *GraphType*: class (input)
    Type of graph to create. :class:`PNGraph`, :class:`PUNGraph`, or :class:`PNEANet`

- *Nodes*: int (input)
    The number of nodes used to generate the graph

Return value:

- graph
    A Snap.py graph of the specified type

The following example shows how to generate different types of fully connected graphs for classes :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    G1 = snap.GenFull(snap.PNGraph, 5)
    for edge in G1.Edges():
        print "%d, %d" % (edge.GetSrcNId(), edge.GetDstNId())

    G2 = snap.GenFull(snap.PUNGraph, 5)
    for edge in G2.Edges():
        print "%d, %d" % (edge.GetSrcNId(), edge.GetDstNId())

    N1 = snap.GenFull(snap.PNEANet, 5)
    for edge in N1.Edges():
        print "%d, %d" % (edge.GetSrcNId(), edge.GetDstNId())
