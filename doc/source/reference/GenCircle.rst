GenCircle
'''''''''

.. function:: GenCircle(GraphType, Nodes, OutDegree, IsDir=True)

Generate a circular graph of type *GraphType* with *Nodes* nodes.  The generated graph will have an edge from each node to the subsequent *OutDegree* nodes.

Parameters:

- *GraphType*: class (input)
    Type of graph to create. :class:`PNGraph`, :class:`PUNGraph`, or :class:`PNEANet`

- *Nodes*: int (input)
    Number of nodes in the generated graph

- *OutDegree*: int (input)
    The number of edges to be added to each node.  This number does not include reciprocal edges.

- *IsDir*: boolean (input)
    Indicates whether the edges should be directed or undirected. Defaults to directed. 

Return value:

- graph
    A Snap.py graph of the specified type

The following example shows how to generate circular graphs for classes :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    G1 = snap.GenCircle(snap.PNGraph, 100, 10)
    for edge in G1.Edges():
        print "%d, %d" % (edge.GetSrcNId(), edge.GetDstNId())

    G2 = snap.GenCircle(snap.PUNGraph, 100, 10)
    for edge in Gw.Edges():
        print "%d, %d" % (edge.GetSrcNId(), edge.GetDstNId())

    G3 = snap.GenCircle(snap.PNEANet, 100, 10)
    for edge in G3.Edges():
        print "%d, %d" % (edge.GetSrcNId(), edge.GetDstNId())
