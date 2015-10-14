LoadEdgeList
''''''''''''

.. function:: LoadEdgeList(GraphType, InFNm, SrcColId, DstColId)

Loads a (directed, undirected or multi) graph from a text file *InFNm* with 1 edge per line (whitespace separated columns, int node ids).

*InFNm* is a whitespace separated file of several columns: ... <source node id> ... <destination node id> ... Since the function assumes each line of the file encodes a single edge and a line in the file can have more than 2 columns, *SrcColId* and *DstColId* must be provided to indicate which column gives the source and which column gives the destination of the edge.

Parameters:

- *GraphType*: graph class (input)
    Class of output graph -- one of :class:`PNGraph`, :class:`PNEANet`, or :class:`PUNGraph`.

- *InFNm*: string (input)
    Filename with the description of the graph edges.

- *SrcColId*: int (input)
    The column number in the file, which contains the node id representing the source vertex.

- *DstColId*: int (input)
    The column number in the file, which contains the node id representing the destination vertex.

Return value:

- graph
    A Snap.py graph or a network represented by the *InFNm* of type *GraphType*.


The following example shows how to load a small file representing a graph::

    import snap

    Graph = snap.LoadEdgeList(snap.PNGraph, "toy_graph", 0, 1)
    Graph.Dump()

    UGraph = snap.LoadEdgeList(snap.PUNGraph, "toy_graph", 0, 1)
    UGraph.Dump()

    Network = snap.LoadEdgeList(snap.PNEANet, "toy_graph", 0, 1)
    Network.Dump()


An example file is given below (toy_graph) ::

    1 1
    1 2
    2 1
    1 3



