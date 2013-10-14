SavePajek
'''''''''''
.. note::

    This page is a draft and under revision.


.. function:: SavePajek(Graph, OutFNm, NIdColorH, NIdLabelH, EIdColorH)

Saves a graph in Pajek .Net format.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

- *OutFNm*: string (input)
    Specifies output filename of Pajek formatted graph

- *NIdColorH*: a hash of int keys and string values (input)
	Maps nodes to node colors.  Keys are node IDs, values are node colors.  Default node color is red. 

- *NIdLabelH*: a hash of int keys and string values (input)
    Maps nodes to node string labels.  Keys are node IDs, values are node string labels.

- *EIdColorH*: int (input)
	Maps edges to edge colors.  Keys are node IDs, values are edge colors.  Default node color is black. 

Return value:

- None

For additional information see http://vlado.fmf.uni-lj.si/pub/networks/pajek/doc/pajekman.pdf

The following example shows how to create a Pajek files for nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
	SavePajek(Graph, "c:\Pajek_Graph.out", "Red", "Label", "Black")
        
    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
	SavePajek(Graph, "c:\Pajek_Graph.out", "Red", "Label", "Black")
    
    Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    SavePajek(Graph, "c:\Pajek_Graph.out", "Red", "Label", "Black")