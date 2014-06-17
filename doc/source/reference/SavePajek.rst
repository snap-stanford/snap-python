SavePajek
'''''''''''

.. function:: SavePajek(Graph, OutFNm)

Saves a graph in Pajek .NET format.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network.

- *OutFNm*: string (input)
    Specifies output filename of Pajek formatted graph.

Return value:

- None

For additional information see http://vlado.fmf.uni-lj.si/pub/networks/pajek/doc/pajekman.pdf


The following example shows how to create a Pajek files for nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    snap.SavePajek(Graph, "Pajek_Graph1.out")
        
    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    snap.SavePajek(UGraph, "Pajek_Graph2.out")
    
    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    snap.SavePajek(Network, "Pajek_Graph3.out")