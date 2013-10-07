LoadEdgeList
''''''''''''

.. function:: LoadEdgeList(GraphType, InFNm, SrcColId, DstColId)

    |  Loads a (directed, undirected or multi) graph from a text file InFNm with 1 edge per line (whitespace separated columns, integer node ids).

    |  Loads the format saved by SaveEdgeList()

    |  Whitespace separated file of several columns: ... <source node id> ... <destination node id> ...
    |  SrcColId and DstColId are column indexes of source/destination (integer!) node ids.
    |  This means there is one edge per line and node IDs are assumed to be integers.


Parameters:

- *GraphType*: Type of the graph (input)
    |  Possible values are :
    |  :class:`PUNGraph` for Undirected Graphs
    |  :class:`PNGraph`  for Directed   Graphs
    |  :class:`PNEANet`  for Directed Node-Edge Networks

- *InFNm*: a string containing the file name (input)
    The file name of the file which contains the edges

- *SrcColId*: Source column number  (input)
    |  The column number in the file, which contains the node id representing the source vertex

- *DstColId*: Destination column number  (input)
    |  The column number in the file, which contains the node id representing the destination vertex

Return value:

- A Snap.py graph or a network represented by the InFNm of type "GraphType"


**Example:**

The following example shows how to load a small file representing a directed graph::

    import snap;

    #Load Directed Graph
    Graph = snap.LoadEdgeList(snap.PNGraph, "toy_graph", 0, 1)
    Graph.Dump()

    #Load Undirected Graph
    Graph = snap.LoadEdgeList(snap.PNGraph, "toy_graph", 0, 1)
    Graph.Dump()

    #Load Node Edge Network
    Graph = snap.LoadEdgeList(snap.PNGraph, "toy_graph", 0, 1)
    Graph.Dump()


An example file is given below (toy_graph) ::

    1 1
    1 2
    2 1
    1 3



