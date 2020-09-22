LoadEdgeListStr 
'''''''''''''''

.. function:: LoadEdgeListStr(GraphType, InFNm, SrcColId=0, DstColId=1, Mapping=False)

Loads a (directed, undirected or multi) graph from a text file *InFNm* with 1 edge per line (whitespace separated columns, int node ids).

*InFNm* is a whitespace separated file of several columns: ... <source node name> ... <destination node name> ... Since the function assumes each line of the file encodes a single edge and a line in the file can have more than 2 columns, *SrcColId* and *DstColId* must be provided to indicate which column gives the source and which column gives the destination of the edge. The node ids given in the file can be arbitrary strings. The mapping of node names to ids either is discarded or saved in *StrToNIdH*, depending on the *Mapping* parameter.

Parameters:

- *GraphType*: graph class
    Class of output graph -- one of :class:`TNGraph`, :class:`TNEANet`, or :class:`TUNGraph`.

- *InFNm*: string
    Filename with the description of the graph edges.

- (optional) *SrcColId*: int
    The column number in the file, which contains the node id representing the source vertex.

- (optional) *DstColId*: int
    The column number in the file, which contains the node id representing the destination vertex.

- (optional) *Mapping*: bool
    Specifies whether to return the mapping of node names to node ids.

Return value:

- graph
    A Snap.py graph or a network represented by the *InFNm* of type *GraphType*.

- (optional) *StrToNIdH*: :class:`TStrIntSH`, a string hash table with string keys and int values
    It is returned, if *Mapping* is True and it contains the mapping of strings to node ids.


The following examples shows how to load a graph from a text file, wiki-vote.txt from http://snap.stanford.edu/data/wiki-Vote.html, where node ids are strings::

    import snap

    G = snap.LoadEdgeListStr(snap.TNGraph, "wiki-Vote.txt", 0, 1)
    print("Number of Nodes: %d" % G.GetNodes())

    G = snap.LoadEdgeListStr(snap.TUNGraph, "wiki-Vote.txt", 0, 1)
    print("Number of Nodes: %d" % G.GetNodes())

    G = snap.LoadEdgeListStr(snap.TNEANet, "wiki-Vote.txt", 0, 1)
    print("Number of Nodes: %d" % G.GetNodes())

    (G, Map) = snap.LoadEdgeListStr(snap.TNGraph, "wiki-Vote.txt", 0, 1, True)
    print("Number of Nodes: %d" % G.GetNodes())
    print("Number of Nodes: %d" % Map.Len())

    # convert input string to node id
    NodeId = Map.GetKeyId("1065")
    # convert node id to input string
    NodeName = Map.GetKey(NodeId)
    print("name", NodeName)
    print("id  ", NodeId)

