DrawGViz
'''''''''''

.. function:: DrawGViz(Graph, Layout, PltFNm, Desc=TStr(), NodeLabels=false, NIdColorH=TIntStrH())

Draws the given Graph using a selected GraphViz Layout engine with nodes colored. Useful for drawing small (<100 node) graphs.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

- *Layout*: TGVizLayout (input)
    One of gvlDot, gvlNeato, gvlTwopi, gvlCirco, gvlSfdp.

- *PltFNm*: str (input)
    Output filename (extension .ps, .png, .gif) determines the output format.

- *Desc*: str (input)
    A string describing the visualization.

- *NodeLabels*: bool (input)
    Whether or not the nodes in image have labels associated with them.
    
- *NIdColorH*: TIntStrH (input)
    Maps node ids to node colors (see GraphViz documentation for more details).

Return value:

- None

Note that larger graphs (more than a few hundred nodes) may take several minutes to finish generating the image. The following example shows how to make a pretty graph image for nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::
    
    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 10, 20)
    snap.DrawGViz(Graph, snap.gvlDot, "graph.png", "my best graph")

    Graph = snap.GenRndGnm(snap.PUNGraph, 10, 40)
    snap.DrawGViz(Graph, snap.gvlNeato, "graph_undirected.png", "pretty good", True)

    NIdColorH = snap.TIntStrH()
    NIdColorH.AddDat(0, "green")
    NIdColorH.AddDat(1, "red")
    NIdColorH.AddDat(2, "purple")
    NIdColorH.AddDat(3, "blue")
    NIdColorH.AddDat(4, "yellow")
    Graph = snap.GenRndGnm(snap.PNEANet, 5, 10)
    snap.DrawGViz(Graph, snap.gvlSfdp, "network.png", "another nice graph", True, NIdColorH)