GenStar
'''''''''''

.. function:: GenStar (GraphType, Nodes, IsDir=True)

Generates a graph with star topology. Node id 0 is in the center and then links to all other nodes.

Parameters:

- *GraphType*: class (input)
    Type of graph to create. :class:`PNGraph`, :class:`PUNGraph`, or :class:`PNEANet`

- *Nodes*: int (input)
    Number of nodes in the star graph, including the center node.

- *IsDir*: boolean (input)
    Indicates whether the star graph is directed or undirected. Defaults to directed. 

Return value:

- graph
    A Snap.py graph of the specified type

The following example shows how to generate a star graph with five nodes using :func:`GenStar` for classes :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    StarGraph = snap.GenStar(snap.PNGraph, 5, True)
    for edge in StarGraph.Edges():
        print "%d, %d" % (edge.GetSrcNId(), edge.GetDstNId())

    StarGraph = snap.GenStar(snap.PUNGraph, 5, True)
    for edge in StarGraph.Edges():
        print "%d, %d" % (edge.GetSrcNId(), edge.GetDstNId())

    StarGraph = snap.GenStar(snap.PNEANet, 5, True)
    for edge in StarGraph.Edges():
        print "%d, %d" % (edge.GetSrcNId(), edge.GetDstNId())
