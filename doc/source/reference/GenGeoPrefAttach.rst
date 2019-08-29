GenGeoPrefAttach
''''''''''''''''

.. function:: GenGeoPrefAttach(NumNodes, NumEdges, Beta, Rnd=TRnd)

Generate a random scale-free, undirected graph using the Geometric Preferential Attachment model by Flexman, Frieze and Vera.

Parameters:

- *NumNodes*: int (input)
    The number of nodes to be created in the graph.

- *NumEdges*: int (input)
    The number of edges to add to each node.

- *Beta*: float (input)
    The beta parameter for the Geometric Preferential Attachment model.  Controls the size of the radius that the algorithm will select nodes from within to which the given node will be connected to by an edge.  The value
    of *Beta* should be between 0 and 0.5, but may be any value.
    The radius is calculated as r = n^{\beta - 1/2}\ln(n).

- *Rnd*: :class:`TRnd` (input)
    Random number generator .

Return Value: 
    
- undirected graph
    A Snap.py undirected graph generated using the Geometric Preferential Attachment model.

For more information see: A geometric preferential attachment model of networks by Flexman, Frieze and Vera. WAW 2004. URL: http://math.cmu.edu/~af1p/Texfiles/GeoWeb.pdf


The following example shows how to generate a random scale-free, undirected graph of type :class:`TUNGraph` using the Geometric Preferential Attachment::

    import snap

    Rnd = snap.TRnd();
    UGraph = snap.GenGeoPrefAttach(100, 10, 0.25, Rnd)
    for EI in UGraph.Edges():
        print("edge: (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId()))

