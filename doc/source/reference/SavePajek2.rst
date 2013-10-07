SavePajek
'''''''''''

.. function:: SavePajek(Graph, OutFNm, NIdColorH = None, NIdLabelH = None)

Saves a graph in a Pajek .NET format.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

- *OutFNm*: str (input)
    Output file name

- *NIdColorH*: a hash of int keys and str values (input)
    Hash table to map node ids to node colors. Default node color is Red.

- *NIdLabelH*: a hash of int keys and str values (input)
    Hash table to map node ids to node string labels.

Return value:

- None

See http://vlado.fmf.uni-lj.si/pub/networks/pajek/doc/pajekman.pdf for a list of supported color names.

The following example shows how to save :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet` in a Pajek .NET format::

	import snap

	NIdColorH = snap.TIntStrH()
	NIdLabelH = snap.TIntStrH()

	Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
	snap.SavePajek(Graph, "pajek_pngraph.txt", NIdColorH, NIdLabelH)

	Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
	snap.SavePajek(Graph, "pajek_pungraph.txt", NIdColorH, NIdLabelH)

	Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
	snap.SavePajek(Graph, "pajek_pneanet.txt", NIdColorH, NIdLabelH)
