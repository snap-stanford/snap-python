GenGeoPrefAttach
''''''''''''''''
.. note::

    This page is a draft and under revision.


.. function:: GenGeoPrefAttach(NumNodes, NumEdges, Beta, Rnd)

Generate a random scale-free graph using the Geometric Preferential Attachment model by Flexman, Frieze and Vera.
The resulting graph will be undirected.

Parameters:

- *NumNodes*: int (input)
    The number of nodes to be created in the graph

- *NumEdges*: int (input)
    The number of edges to add to each node.  This will not necessarily be the final degree of each node as the
    edges added will also increase the degrees of the other nodes connected by the edges

- *Beta*: float (input)
    The beta parameter for the Geometric Preferential Attachment model.  Controls the size of the radius from
    within which the algorithm will select nodes to which the given node will be connected by an edge.  The value
    of *Beta* should be between 0 and 0.5, but may be any value.
    The radius is calculated as :math:`r = n^{\beta - 1/2}\ln n`

- *Rnd*: TRnd (input)
    A random distribution generator to use when selecting nodes to which a given node will connect.

Return value:

- `snap.TUNGraph`: the generated graph

For more information see: A geometric preferential attachment model of networks by Flexman, Frieze and Vera. WAW 2004. URL: http://math.cmu.edu/~af1p/Texfiles/GeoWeb.pdf

The following example shows how to generate an undirected graph of type `snap.TUNGraph`::

    import snap

    # Create a new random distribution generator
    Rnd = snap.TRnd();

    # Create a new scale-free undirected graph
    Graph = snap.GenGeoPrefAttach(100, 10, 0.25, Rnd)

