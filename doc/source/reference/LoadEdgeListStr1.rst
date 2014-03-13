LoadEdgeListStr
'''''''''''''''

.. function:: LoadEdgeListStr(GraphType, InFNm, SrcColId, DstColId, StrToNIdH)

Loads a (directed, undirected or multi) graph from a text file *InFNm* with 1 edge per line (whitespace separated columns, int node ids).

*InFNm* is a whitespace separated file of several columns: ... <source node name> ... <destination node name> ... Since the function assumes each line of the file encodes a single edge and a line in the file can have more than 2 columns, *SrcColId* and *DstColId* must be provided to indicate which column gives the source and which column gives the destination of the edge. The node ids given in the file can be arbitrary strings. The mapping of node names to ids is saved in *StrToNIdH*.

Parameters:

- *GraphType*: graph class (input)
    Class of output graph -- one of :class:`PNGraph`, :class:`PNEANet`, or :class:`PUNGraph`.

- *InFNm*: string (input)
    Filename with the description of the graph edges.

- *SrcColId*: int (input)
    The column number in the file, which contains the node id representing the source vertex.

- *DstColId*: int (input)
    The column number in the file, which contains the node id representing the destination vertex.

- *StrToNIdH*: TStrIntH, a hash table with string keys and int values (output)
    Contains the mapping of strings to node ids.


Return value:

- graph
    A Snap.py graph or a network represented by the *InFNm* of type *GraphType*.


The following example shows how to load the following from a text file, wiki-vote.txt from http://snap.stanford.edu/data/wiki-Vote.html, where node IDs are strings: :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    mapping = snap.TStrIntH()
    G0 = snap.LoadEdgeListStr(snap.PNGraph, "wiki-Vote.txt", 0, 1, mapping)
