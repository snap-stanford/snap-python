SavePajek
'''''''''''

.. function:: SavePajek(Graph, OutFNm, NIdColorH = 'red', NIdLavelH, EIdColorH = 'black')

Saves the *Graph* in a Pajek .NET format

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

- *OutFNm*: string (input)
    The Output filename
	
- *NIdColorH*: TIntStrH (input)
    NIdColorH maps node ids to node colors. Default node color is Red. See http://vlado.fmf.uni-lj.si/pub/networks/pajek/doc/pajekman.pdf for a list of supported color names.

- *NIdLabelH*: TIntStrH (input)
    NIdLabelH maps node ids to node string labels. 

- *EIdColorH *: TIntStrH (input)
    EIdColorH maps edge ids to node colors. Default edge color is Black. See http://vlado.fmf.uni-lj.si/pub/networks/pajek/doc/pajekman.pdf for a list of supported color names.


Return value:

- None

The following example saves the graph in the Pajek format in: 
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
	snap.SavePajek(Graph, 'PNGout.net');

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    snap.SavePajek(Graph, 'PUNGout.net');

    Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    snap.SavePajek(Graph, 'PNEANput.net');
