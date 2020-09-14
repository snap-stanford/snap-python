DrawGViz
''''''''

.. function:: DrawGViz(Layout, PltFNm, Desc, NodeLabelH)

A graph method to draw a given graph using a selected GraphViz Layout engine with nodes labeled. Creates a file with name *PltFNm*.

Parameters:

- *Layout*: TGVizLayout
    One of gvlDot, gvlNeato, gvlTwopi, gvlCirco, gvlSfdp. The type of layout for the graph.

- *PltFNm*: string
    Output filename (extension .ps, .png, .gif) determines the output format.

- *Desc*: string
    A string describing the visualization.
    
- *NodeLabelH*: Python dictionary or :class:`TIntStrH`, a hash table of int keys and string values
    Maps node ids to node labels.

Return value:

- None


The following example shows how to draw the graph for :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap
    
    Graph = snap.GenRndGnm(snap.TNGraph, 10, 50)
    labels = {}
    for NI in Graph.Nodes():
	    labels[NI.GetId()] = str(NI.GetId())
    Graph.DrawGViz(snap.gvlDot, "output.png", " ", labels)

    UGraph = snap.GenRndGnm(snap.TUNGraph, 10, 50)
    labels = {}
    for NI in UGraph.Nodes():
        labels[NI.GetId()] = str(NI.GetId())
    UGraph.DrawGViz(snap.gvlDot, "output.png", " ", labels)

    Network = snap.GenRndGnm(snap.TNEANet, 10, 50)
    labels = {}
    for NI in Network.Nodes():
        labels[NI.GetId()] = str(NI.GetId())
    Network.DrawGViz(snap.gvlDot, "output.png", " ", labels)
