GenStar
'''''''''''

.. function:: GenStar (GraphType, Nodes, IsDir=True)

Generates a graph with star topology. Node id 0 is in the center and then links to all other nodes.

Parameters:

- *GraphType*: graph class (input)
    Class of output graph -- one of :class:`PNGraph`, :class:`PNEANet`, or :class:`PUNGraph`.

- *Nodes*: int (input)
    Number of nodes in the star graph, including the center node.

- *IsDir*: boolean (input)
    Indicates whether the edges should be directed or undirected. Defaults to directed. 

Return value:

- graph
    A Snap.py graph of the specified type.


The following example shows how to generate a star graph with five nodes using :func:`GenStar` for classes :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenStar(snap.PNGraph, 5, True)
    for EI in Graph.Edges():
        print "edge: (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId())

    UGraph = snap.GenStar(snap.PUNGraph, 5, True)
    for EI in UGraph.Edges():
        print "edge: (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId())

    Network = snap.GenStar(snap.PNEANet, 5, True)
    for EI in StarGraph.Edges():
        print "edge: (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId())
