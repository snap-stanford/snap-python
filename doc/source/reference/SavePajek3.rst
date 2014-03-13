SavePajek
'''''''''

.. function:: SavePajek (Graph, OutFNm, NIdColorH, NIdLabelH, EIdColorH)

Saves a graph in a Pajek .NET format.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network.

- *OutFNm*: string (input)
    Specifies output filename of Pajek formatted graph.
    
- *NIdColorH*: TIntStrH, a hash table of int keys and string values (input)
    Maps node ids to node colors. Default node color is Red.

- *NIdLabelH*: TIntStrH, a hash table of int keys and string values (input)
    Maps node ids to node string labels.

- *EIdColorH*: TIntStrH, a hash table of int keys and string values (input)
    Maps edge ids to node colors. Default edge color is black.

Return value:

- None

For additional information see http://vlado.fmf.uni-lj.si/pub/networks/pajek/doc/pajekman.pdf


The following example saves the graph in the Pajek format in: 
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    NIdColorH = snap.TIntStrH()
    for i in range(100):
        if i % 2 == 0:
            NIdColorH[i] = "red"
        else:
            NIdColorH[i] = "blue"
    NIdLabelH = snap.TIntStrH()
    for i in range(100):
        NIdLabelH[i] = str(i)
    EIdColorH = snap.TIntStrH()
    for i in range(1000):
        EIdColorH[i] = "red"

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    snap.SavePajek(Graph, "Pajek_Graph1.out", NIdColorH, NIdLabelH, EIdColorH)
        
    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    snap.SavePajek(UGraph, "Pajek_Graph2.out", NIdColorH, NIdLabelH, EIdColorH)
    
    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    snap.SavePajek(Network, "Pajek_Graph3.out", NIdColorH, NIdLabelH, EIdColorH)
