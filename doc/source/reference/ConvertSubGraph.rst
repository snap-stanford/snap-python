ConvertSubGraph
'''''''''''''''

.. function:: ConvertSubGraph(GraphType, InGraph, NIdV, RenumberNodes = False)

Returns an induced subgraph of graph *InGraph* with *NIdV* nodes with an optional node renumbering. The resulting subgraph will have type *GraphType*. Node and edge data is not copied, but it is shared by input and output graphs.

Parameters:

- *GraphType*: graph class (input)
    Class of output graph -- one of `PNGraph`, `PNEANet`, or `PUNGraph`

- *InGraph*: graph (input)
    A Snap.py graph or a network

- *NIdV*: TIntV, a vector of ints (input)
    The vector of node ids that will be included in the induced subgraph.

- *RenumberNodes*: Boolean (input)
    Determines whether the node IDs are preserved or not. If False, then nodes in the resulting graph have the same node IDs as nodes in *InGraph*. If True, then nodes in the resulting graph are renumbered sequentially from 0 to N-1. By default, the nodes are not renumbered.

Return value:

- graph
    A graph of type *GraphType* that is a subgraph of *InGraph*
    
The following example shows how to convert a SubGraph in
:class:`TNGraph`::

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
  
