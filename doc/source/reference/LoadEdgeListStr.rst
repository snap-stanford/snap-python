LoadEdgeListStr 
'''''''''''

.. function:: Graph LoadEdgeListStr (GraphType, InFNm, SrcColId = 0, DstColId = 1)

Loads a (directed, undirected or multi) graph from a text file InFNm with 1 edge per line (whitespace separated columns, arbitrary string node ids).

Loads the format saved by SaveEdgeList(), where node IDs are strings.

SrcColId and DstColId are column indexes of source/destination (string) node ids. This means there is one edge per line and node IDs can be arbitrary STRINGs. Note that the mapping of node names to ids is discarded.

Parameters:

- *GraphType*: graph type (input)
    One of: PNGraph (directed graph), PUNGraph (undirected graph), PNEANet (directed network)

- *InFNm*: string (input)
    Name of text file

- *SrcColId*: int (input)
    Column index of source (string) node ids

- *DstColId*: int (input)
    Column index of destination (string) node ids

Return value:

- *Graph*: graph
    A Snap.py graph or a network

The following example shows how to load the following from a text file where node IDs are strings: :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    G = snap.LoadEdgeListStr(snap.PNGraph, "Wiki-Vote.txt", 0, 1)
    print "Number of Nodes:", G.GetNodes()

    G = snap.LoadEdgeListStr(snap.PUNGraph, "Wiki-Vote.txt", 0, 1)
    print "Number of Nodes:", G.GetNodes()

    G = snap.LoadEdgeListStr(snap.PNEANet, "Wiki-Vote.txt", 0, 1)
    print "Number of Nodes:", G.GetNodes()