LoadEdgeList
''''''''''''

.. function:: LoadEdgeList(PGraph, InFNm, SrcColId, DstColId, Separator)

Loads a (directed, undirected or multi) graph from a text file *InFNm* with 1 edge per line (columns separated by *Separator*, int node ids).

*InFNm* is a *Separator* separated file of several columns: ... <source node id> ... <destination node id> ... Since the function assumes each line of the file encodes a single edge and a line in the file can have more than 2 columns, *SrcColId* and *DstColId* must be provided to indicate which column gives the source and which column gives the destination of the edge. Node ids must be ints.

Parameters:

- *GraphType*: graph class (input)
    Class of output graph -- one of :class:`PNGraph`, :class:`PNEANet`, or :class:`PUNGraph`.

- *InFNm*: string (input)
    Filename with the description of the graph edges.

- *SrcColId*: int (input)
    The column number in the file, which contains the node id representing the source vertex.

- *DstColId*: int (input)
    The column number in the file, which contains the node id representing the destination vertex.

- *Separator*: char (input)
    Column separator.

Return value:

- graph
    A Snap.py graph or a network represented by the *InFNm* of type *GraphType*.


The following example shows how to load edge lists for
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap
    
    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    snap.SaveEdgeList(Graph, "PNGraph.edges")
    LoadedGraph = snap.LoadEdgeList(snap.PNGraph, "PNGraph.edges", 0, 1, '\t')
    LoadedGraph.Dump()
    
    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    snap.SaveEdgeList(UGraph, "PUNGraph.edges")
    LoadedUGraph = snap.LoadEdgeList(snap.PUNGraph, "PUNGraph.edges", 0, 1, '\t')
    LoadedUGraph.Dump()
    
    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    snap.SaveEdgeList(Network, "PNEANet.edges")
    LoadedNet = snap.LoadEdgeList(snap.PNEANet, "PNEANet.edges", 0, 1, '\t')
    LoadedNet.Dump()
