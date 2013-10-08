SaveGViz
''''''''

.. function:: SaveGViz(Graph, OutFNm, Desc, NodeLabels, NIdColorH)

Computes the PageRank score of every node in *Graph*. The scores are stored in *PRankH*.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

- *OutFNm*: string (input)
    Name of the output file

- *Desc*: string (input)
    Desc of the Graph

- *NodeLabels*: bool (input)
    True: Show the node lables 
	False: Hide the node lables

- *NIdColorH*: int string Hash (input)
    Hash Table containing color for each node with NId as Key and Color as Value

Return value:

- None

For more info about Graph Viz see: http://www.graphviz.org

The following example shows how to save graphs of following types for GraphViz
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    H = snap.TIntStrH()
    H.AddDat(1, "blue")
    H.AddDat(2, "blue")
    H.AddDat(3, "red")
    H.AddDat(4, "red")

    Graph = snap.GenRndGnm(snap.PNGraph, 4, 6)
    snap.SaveGViz(Graph, "Graph.gv", "Directed Random Graph", True, H)

    Graph = snap.GenRndGnm(snap.PUNGraph, 4, 6)
    snap.SaveGViz(Graph, "Graph.gv", "Undirected Random Graph", True, H)

    Graph = snap.GenRndGnm(snap.PNEANet, 4, 6)
    snap.SaveGViz(Graph, "Graph.gv", "Directed Random Graph with Attributes", True, H)

