DrawGViz
'''''''''''

.. function:: DrawGViz(Graph, Layout, PltFNm, Desc, NodeLabelH)

Draws a given *Graph* using a selected GraphViz Layout engine with nodes labeled. Creates a file with name *PltFNm*.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network.

- *Layout*: TGVizLayout (input)
    One of gvlDot, gvlNeato, gvlTwopi, gvlCirco, gvlSfdp. The type of layout for the graph.

- *PltFNm*: string (input)
    Output filename (extension .ps, .png, .gif) determines the output format.

- *Desc*: string (input)
    A string describing the visualization.
    
- *NodeLabelH*: :class:`TIntStrH`, a hash table of int keys and string values (input)
    Maps node ids to node labels.

Return value:

- None


The following example shows how to draw the graph for :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap
    
    Graph = snap.GenRndGnm(snap.PNGraph, 10, 50)
    labels = snap.TIntStrH()
    for NI in Graph.Nodes():
	    labels[NI.GetId()] = str(NI.GetId())
    snap.DrawGViz(Graph, snap.gvlDot, "output.png", " ", labels)

    UGraph = snap.GenRndGnm(snap.PUNGraph, 10, 50)
    labels = snap.TIntStrH()
    for NI in UGraph.Nodes():
        labels[NI.GetId()] = str(NI.GetId())
    snap.DrawGViz(UGraph, snap.gvlDot, "output.png", " ", labels)

    Network = snap.GenRndGnm(snap.PNEANet, 10, 50)
    labels = snap.TIntStrH()
    for NI in Network.Nodes():
        labels[NI.GetId()] = str(NI.GetId())
    snap.DrawGViz(Network, snap.gvlDot, "output.png", " ", labels)
