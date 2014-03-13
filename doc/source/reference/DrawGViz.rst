DrawGViz
'''''''''''

.. function:: DrawGViz(Graph, Layout, PltFNm, Desc=TStr(), NodeLabels=False, NIdColorH=TIntStrH())

Draws the given *Graph* using a selected GraphViz Layout engine with nodes colored. Useful for drawing small (<100 node) graphs. Creates a file with name *PltFNm*.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

- *Layout*: TGVizLayout (input)
    One of gvlDot, gvlNeato, gvlTwopi, gvlCirco, gvlSfdp. The type of layout for the graph.

- *PltFNm*: string (input)
    Output filename (extension .ps, .png, .gif) determines the output format.

- *Desc*: string (input)
    A string describing the visualization.

- *NodeLabels*: bool (input)
    Whether or not the nodes in image have labels associated with them.
    
- *NIdColorH*: TIntStrH, a hash table with int keys and string values (input)
    Maps node ids to node colors (see GraphViz documentation for more details).

Return value:

- None


Note that larger graphs (more than a few hundred nodes) may take several minutes to finish generating the image. The following example shows how to make a pretty graph image for nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::
    
    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 10, 20)
    snap.DrawGViz(Graph, snap.gvlDot, "graph.png", "graph 1")

    UGraph = snap.GenRndGnm(snap.PUNGraph, 10, 40)
    snap.DrawGViz(UGraph, snap.gvlNeato, "graph_undirected.png", "graph 2", True)

    NIdColorH = snap.TIntStrH()
    NIdColorH[0] = "green"
    NIdColorH[1] = "red"
    NIdColorH[2] = "purple"
    NIdColorH[3] = "blue"
    NIdColorH[4] = "yellow"
    Network = snap.GenRndGnm(snap.PNEANet, 5, 10)
    snap.DrawGViz(Network, snap.gvlSfdp, "network.png", "graph 3", True, NIdColorH)