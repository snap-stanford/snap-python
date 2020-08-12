DrawGVizColor
'''''''''''''

.. function:: DrawGVizColor(Layout, PltFNm, Desc=TStr(), NodeLabels=False, NIdColorH=TIntStrH())

A graph method that draws a graph using a selected GraphViz Layout engine with nodes colored. Useful for drawing small (<100 node) graphs. Creates a file with name *PltFNm*.

Parameters:

- *Layout*: TGVizLayout
    One of gvlDot, gvlNeato, gvlTwopi, gvlCirco, gvlSfdp. The type of layout for the graph.

- *PltFNm*: string
    Output filename (extension .ps, .png, .gif) determines the output format.

- *Desc*: string
    A string describing the visualization.

- *NodeLabels*: bool
    Whether or not the nodes in image have labels associated with them.
    
- *NIdColorH*: Python dictionary or :class:`TIntStrH`, a hash table with int keys and string values
    Maps node ids to node colors (see GraphViz documentation for more details).

Return value:

- None


Note that larger graphs (more than a few hundred nodes) may take several minutes to finish generating the image. The following example shows how to make a pretty graph image for nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::
    
    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 10, 20)
    Graph.DrawGVizColor(snap.gvlDot, "graph.png", "graph 1")

    UGraph = snap.GenRndGnm(snap.PUNGraph, 10, 40)
    UGraph.DrawGVizColor(snap.gvlNeato, "graph_undirected.png", "graph 2", True)

    NIdColorH = { 0 : "green", 1 : "red", 2 : "purple", 3 : "blue", 4 : "yellow" }
    Network = snap.GenRndGnm(snap.PNEANet, 5, 10)
    Network.DrawGVizColor(snap.gvlSfdp, "network.png", "graph 3", True, NIdColorH)

