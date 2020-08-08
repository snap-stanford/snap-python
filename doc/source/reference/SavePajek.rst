SavePajek
'''''''''

.. function:: SavePajek (Graph, OutFNm, NIdColorH = None, NIdLabelH = None, EIdColorH = None)

A graph method that saves a graph in a Pajek .NET format.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network.

- *OutFNm*: string (input)
    Specifies output filename of Pajek formatted graph.
    
- (optional) *NIdColorH*: Python dictionary or :class:`TIntStrH`, a hash table of int keys and string values (input)
    Maps node ids to node colors. Default node color is Red.

- (optional) *NIdLabelH*: Python dictionary or :class:`TIntStrH`, a hash table of int keys and string values (input)
    Maps node ids to node string labels.

- (optional) *EIdColorH*: Python dictionary or :class:`TIntStrH`, a hash table of int keys and string values (input)
    Maps edge ids to node colors. Default edge color is black.

Return value:

- None

For additional information see http://vlado.fmf.uni-lj.si/pub/networks/pajek/doc/pajekman.pdf


The following example saves the graph in the Pajek format in: 
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    NIdColorH = {}
    for i in range(100):
        if i % 2 == 0:
            NIdColorH[i] = "red"
        else:
            NIdColorH[i] = "blue"
    NIdLabelH = {}
    for i in range(100):
        NIdLabelH[i] = str(i)
    EIdColorH = {}
    for i in range(1000):
        EIdColorH[i] = "red"

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    Graph.SavePajek("Pajek_Graph1.out", NIdColorH, NIdLabelH, EIdColorH)
        
    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    UGraph.SavePajek("Pajek_Graph2.out", NIdColorH, NIdLabelH, EIdColorH)
    
    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    Network.SavePajek("Pajek_Graph3.out", NIdColorH, NIdLabelH, EIdColorH)
