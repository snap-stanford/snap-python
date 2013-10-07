LoadEdgeList
''''''''''''

.. function:: LoadEdgeList(PGraph, InFNm, SrcColId, DstColId, Separator)

Loads a (directed, undirected or multi) graph from a text file *InFNm* of type *PGraph* (e.g. (snap.PNGraph | snap.PUNGraph | snap.PNEANet)) with 1 edge per line ('*Separator*' separated columns, integer node ids).

Loads the format saved by TSnap.SaveEdgeList() if we set Separator=''.

'*Separator*' separated file of several columns: ... <source node="" id>=""> ... <destination node="" id>=""> ... *SrcColId* and *DstColId* are column indexes of source/destination (integer!) node ids. This means there is one edge per line and node IDs are assumed to be integers.

References TSsParser.GetInt(), and TSsParser.Next().

Parameters:

- *PGraph*: graph type (input)
    A graph type, e.g. (snap.PNGraph | snap.PUNGraph | snap.PNEANet)

- *InFNm*: file (input)
    A text file with a (directed, undirected or multi) graph with 1 edge per line.

- *SrcColId*: integer (input)
    Column indexes of source (integer!) node ids.

- *DstColId*: integer (input)
    Column indexes of destination (integer!) node ids.

- *Separator*: char (input)
    Column separator.

Return value:

- *PGraph*: graph (return)
    A loaded graph of type *PGraph*

The following example shows how to load edge lists for
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap
    
    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    snap.SaveEdgeList(Graph, "PNGraph.edges")
    LoadedGraph = snap.LoadEdgeList(snap.PNGraph, "PNGraph.edges", 0, 1, '\t')
    LoadedGraph.Dump()
    
    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    snap.SaveEdgeList(Graph, "PUNGraph.edges")
    LoadedGraph = snap.LoadEdgeList(snap.PUNGraph, "PUNGraph.edges", 0, 1, '\t')
    LoadedGraph.Dump()
    
    Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    snap.SaveEdgeList(Graph, "PNEANet.edges")
    LoadedGraph = snap.LoadEdgeList(snap.PNEANet, "PNEANet.edges", 0, 1, '\t')
    LoadedGraph.Dump()
