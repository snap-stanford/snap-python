LoadEdgeListStr
'''''''''''''''
.. note::

    This page is a draft and under revision.


.. function:: LoadEdgeListStr(GraphType, InFNm, SrcColId, DstColId, StrToNIdH)

.. note::

    This function is not yet supported.

Loads a (directed, undirected or multi) graph from a text file InFNm with 1 edge per line (whitespace separated columns, arbitrary string node ids).

Loads the format saved by TSnap::SaveEdgeList(), where node IDs are strings and mapping of strings to node ids are stored.

Whitespace separated file of several columns: ... <source node="" id>=""> ... <destination node="" id>=""> ... SrcColId and DstColId are column indexes of source/destination (string) node ids. This means there is one edge per line and node IDs can be arbitrary STRINGs. The mapping of strings to node ids in stored in StrToNIdH. To map between node names and ids use: NId = StrToNIdH.GetKeyId(NodeName) and TStr NodeName = StrToNIdH.GetKey(NId);

Parameters:

- *GraphType*: Graph type (output)
    Specifies the type (PNGraph, PUNGraph) of graph that is output.

- *InFNm*: Input Filename (input)
    Name of the file: 1 edge per line, with whitespace separated columns and arbitrary string node ids.

- *SrcColId*: Source Column ID (input)
    Contains the column indices of the source node ids.

- *DstColId*: Destination Column ID (input)
    Contains the column indices of the destination node ids.

- *StrToNIdH*: String To Node ID Hash (output)
    Contains the mapping of strings to node ids.


Return value:

- *Graph*: Returns a PGraph (can be directed, undirected, or multi).

Also see: function:: LoadEdgeListStr(GraphType, InFNm, SrcColId, DstColId)

.. note:: I couldn't get the one with StrToNIdH version to work... I can't seem to define a TStringHash. Is it not implemented yet?

See below for example uses::

    import snap

    # assuming you have the wiki-vote.txt file from: http://snap.stanford.edu/data/wiki-Vote.html

    # Without StrToNIdH
    G0 = snap.LoadEdgeListStr(snap.PNGraph, "wiki-Vote.txt", 0, 1)
    
    # With StrToNIdH
    # Initialize StrToNIdH (string to node mapping)
    mapping = snap.TStrHash()
    G0 = snap.LoadEdgeListStr(snap.PNGraph, "wiki-Vote.txt", 0, 1, mapping)
