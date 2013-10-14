DrawGViz
'''''''''''
.. note::

    This page is a draft and under revision.


.. function:: DrawGViz(Graph, Layout, PltFNm, Desc, NodeLabelH)

Draws a given Graph using a selected GraphViz Layout engine with nodes labeled.

    Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

- *Layout*: enum {gvlDot, gvlNeato, gvlTwopi, gvlCirco, gvlSfdp} (input)
    Type of layout for the graph

- *PltFNm*: string (input)
    Output filename (extension .ps, .png, .gif) determines the output format.

- *Desc*: string (input)
    
- *NodeLabelH*: TIntStrH (input)
    Maps node ids to node labels.

    Return value:

    - None


The following example shows how to draw the graph for :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    from snap import *
    Graph = GenRndGnm(PNGraph, 10, 50)
    label = TIntStrH()
    for n in Graph.Nodes():
	labels.AddDat(n.GetId(), str(n.GetId())
    DrawGViz(Graph, gvlDot, "output.png", " ", labels)

    Graph = GenRndGnm(PUNGraph, 10, 50)
    label = TIntStrH()
    for n in Graph.Nodes():
	labels.AddDat(n.GetId(), str(n.GetId())
    DrawGViz(Graph, gvlDot, "output.png", " ", labels)

    Graph = GenRndGnm(PNEANet, 10, 50)
    label = TIntStrH()
    for n in Graph.Nodes():
	labels.AddDat(n.GetId(), str(n.GetId())
    DrawGViz(Graph, gvlDot, "output.png", " ", labels)
