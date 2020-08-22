LoadEdgeList
''''''''''''

.. function:: LoadEdgeList(GraphType, InFNm, SrcColId=0, DstColId=1, Separator=" ")

Loads a (directed, undirected or multi) graph from a text file *InFNm* with 1 edge per line (columns separated by *Separator*, int node ids).

*InFNm* is a *Separator* separated file of several columns: ... <source node id> ... <destination node id> ... Since the function assumes each line of the file encodes a single edge and a line in the file can have more than 2 columns, *SrcColId* and *DstColId* must be provided to indicate which column gives the source and which column gives the destination of the edge. Node ids must be ints.

Parameters:

- *GraphType*: graph class
    Class of output graph -- one of :class:`TNGraph`, :class:`TNEANet`, or :class:`TUNGraph`.

- *InFNm*: string
    Filename with the description of the graph edges.

- (optional) *SrcColId*: int
    The column number in the file, which contains the node id representing the source vertex.

- (optional) *DstColId*: int
    The column number in the file, which contains the node id representing the destination vertex.

- (optional) *Separator*: char
    Column separator. The default value is whitespace.

Return value:

- graph
    A Snap.py graph or a network represented by the *InFNm* of type *GraphType*.


The following example shows how to load edge lists for
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap
   
    Graph = snap.GenRndGnm(snap.TNGraph, 100, 1000)
    Graph.SaveEdgeList("TNGraph.edges")
    LoadedGraph = snap.LoadEdgeList(snap.TNGraph, "TNGraph.edges", 0, 1, '\t')
    LoadedGraph.Dump()

    UGraph = snap.GenRndGnm(snap.TUNGraph, 100, 1000)
    UGraph.SaveEdgeList("TUNGraph.edges")
    LoadedUGraph = snap.LoadEdgeList(snap.TUNGraph, "TUNGraph.edges", 0, 1, '\t')
    LoadedUGraph.Dump()
   
    Network = snap.GenRndGnm(snap.TNEANet, 100, 1000)
    Network.SaveEdgeList("TNEANet.edges")
    LoadedNet = snap.LoadEdgeList(snap.TNEANet, "TNEANet.edges", 0, 1, '\t')
    LoadedNet.Dump()

