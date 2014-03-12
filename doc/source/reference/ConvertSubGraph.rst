ConvertSubGraph
'''''''''''''''

.. function:: ConvertSubGraph(GraphType, InGraph, NIdV, RenumberNodes=False)

Returns an induced subgraph of graph *InGraph* with *NIdV* nodes with an optional node renumbering. The resulting subgraph will have type *GraphType*. Node and edge data is not copied, but it is shared by input and output graphs.

Parameters:

- *GraphType*: graph class (input)
    Class of output graph -- one of :class:`PNGraph`, :class:`PNEANet`, or :class:`PUNGraph`.

- *InGraph*: graph (input)
    A Snap.py graph or a network.

- *NIdV*: TIntV, a vector of ints (input)
    Node IDs that will be included in the subgraph.

- *RenumberNodes*: boolean (input)
    Determines whether the node IDs are preserved or not. If False, then nodes in the resulting graph have the same node IDs as nodes in *InGraph*. If True, then nodes in the resulting graph are renumbered sequentially from 0 to N-1, where N is the number of nodes. By default, the nodes are not renumbered.

Return value:

- graph
    A snap.py graph of type *GraphType* with *NIdV* nodes from the original graph *InGraph*.
    
    
The following example shows how to convert a subgraph between the different types of graphs::

    import snap

    V = snap.TIntV()
    for i in range(10):
        V.Add(i)

    GIn = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    GOut = snap.ConvertSubGraph(snap.PUNGraph, GIn, V)
    for NI in GOut.Nodes():
        print "node: %d" % NI.GetId()

    GIn = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    GOut = snap.ConvertSubGraph(snap.PNEANet, GIn, V)
    for NI in GOut.Nodes():
        print "node: %d" % NI.GetId()

    GIn = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    GOut = snap.ConvertSubGraph(snap.PNGraph, GIn, V)
    for NI in GOut.Nodes():
        print "node: %d" % NI.GetId()
        
  
