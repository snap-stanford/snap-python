SavePajek
'''''''''
.. note::

    This page is a draft and under revision.


.. function:: SavePajek (Graph, OutFNm, NIdColorH, NIdLabelH, EIdColorH)

Saves a graph in a Pajek .NET format.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

- *OutFNm*: string (input)
    Desired filename for output. This function will create a new file if one does not exist or smash an already existing file with this name.

- *NIdColorH*: a hash of int keys and string color names (input)
    Maps node ids to node colors. Default node color is Red.

- *NIdLabelH*: a hash of int keys and string labels (input)
    Maps node ids to node string labels.

- *EIdColorH*: a hash of int keys and string color names (input)
    Maps edge ids to node colors. Default edge color is Black.

Return value:

- None

For more info see: http://vlado.fmf.uni-lj.si/pub/networks/pajek/doc/pajekman.pdf

The following example shows how to use this function in Python::
    
    import snap
    Graph = snap.GenRndGnm(snap.PNGraph, 3, 4)
    nodeColors = snap.TIntStrH()
    nodeColors.AddDat(1, "Red")
    nodeColors.AddDat(2, "Green")
    nodeColors.AddDat(3, "Blue")
    nodeLabels = snap.TIntStrH()
    nodeLabels.AddDat(1, "Home")
    nodeLabels.AddDat(2, "Work")
    nodeLabels.AddDat(3, "School")
    edgeColors = snap.TIntStrH()
    edgeColors.AddDat(1, "Red")
    edgeColors.AddDat(2, "Black")
    edgeColors.AddDat(3, "Green")
    edgeColors.AddDat(4, "Blue")
    snap.SavePajek(Graph, "graphFile.txt", nodeColors, nodeLabels, edgeColors)
