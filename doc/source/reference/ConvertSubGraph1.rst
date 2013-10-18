ConvertSubGraph
'''''''''''''''
.. note::

    This page is a draft and under revision.


.. function:: ConvertSubGraph(InGraph, NIdV, RenumberNodes=false)

Creates a subgraph of the input graph *InGraph* on *NIdV* nodes and returns an output graph, subject to an optional renumbering of the subgraph's nodes. Input and output graphs can have different types. Node and edge data is not copied, but it is shared by input and output graphs.

Parameters:

- *InGraph*: graph (input)
    A Snap.py graph or a network

- *NIdV*: vector of integers (input)
    The vector includes the IDs of the nodes that will be included in the induced subgraph.

- *RenumberNodes*: boolean (input)
    If this is true, then the nodes in *NIdV* are sequentially renumbered from 0 to N-1. The default is false.

Return value:

- A subgraph of *InGraph* using the nodes in *NIdV*. The type of output graph should be specified as the first argument to the function. (PGraph)

The following example shows how to create an induced subgraph on a given subset of nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    List = snap.TIntV.GetV(1, 4, 9, 16, 25, 36)
    G2 = snap.ConvertSubGraph(snap.PUNGraph, Graph, List)
    for EI in G2.Edges():
        print "edge: (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId())
    for NI in G2.Nodes():
        print "node: ", NI.GetId()
        
    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    List = snap.TIntV.GetV(1, 2, 3, 5, 8, 13)
    G2 = snap.ConvertSubGraph(snap.PNGraph, Graph, List)
    for EI in G2.Edges():
        print "edge: (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId())
    for NI in G2.Nodes():
        print "node: ", NI.GetId()

    Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    List = snap.TIntV.GetV(1,3,6,10,15,21)
    G2 = snap.ConvertSubGraph(snap.PNGraph, Graph, List, True)
    for EI in G2.Edges():
        print "edge: (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId())
    for NI in G2.Nodes():
        print "node: ", NI.GetId()
