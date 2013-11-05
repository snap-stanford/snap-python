GenGeoPrefAttach
''''''''''''''''

.. function:: GenGeoPrefAttach(NumNodes, NumEdges, Beta, Rnd)

Generate a random scale-free, undirected graph using the Geometric Preferential Attachment model by Flexman, Frieze and Vera.

Parameters:

- *NumNodes*: int (input)
    The number of nodes to be created in the graph

- *NumEdges*: int (input)
    The number of edges to add to each node

- *Beta*: float (input)
    The beta parameter for the Geometric Preferential Attachment model.  Controls the size of the radius that the algorithm will select nodes from within to which the given node will be connected to by an edge.  The value
    of *Beta* should be between 0 and 0.5, but may be any value.
    The radius is calculated as :math:`r = n^{\beta - 1/2}\ln(n)`

- *Rnd*: TRnd (input)
    Random number generator 

Return Value: 
    
- PUNGraph
    An undirected graph generated using the Geometric Preferential Attachment model

For more information see: A geometric preferential attachment model of networks by Flexman, Frieze and Vera. WAW 2004. URL: http://math.cmu.edu/~af1p/Texfiles/GeoWeb.pdf

The following example shows how to generate an undirected graph of type :class:`TUNGraph`::

    import snap

    Rnd = snap.TRnd();
    Graph = snap.GenGeoPrefAttach(100, 10, 0.25, Rnd)
    for edge in Graph.Edges():
        print "%d, %d" % (edge.GetSrcNId(), edge.GetDstNId())

