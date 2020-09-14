ConvertSubGraph
'''''''''''''''

.. function:: ConvertSubGraph(GraphType, NIdV, RenumberNodes=False)

A graph method that returns an induced subgraph of the original graph with *NIdV* nodes with an optional node renumbering. The resulting subgraph will have type *GraphType*. Any node and edge data is not copied, but it is shared by input and output graphs.

Parameters:

- *GraphType*: graph class
    Class of output graph -- one of TNGraph, TUNGraph, or TNEANet.

- *NIdV*: Python list or :class:`TIntV`, a vector of ints
    Node ids that will be included in the subgraph.

- (optional) *RenumberNodes*: bool
    Determines whether the node ids are preserved or not. If False, then nodes in the resulting graph have the same node ids as nodes in the original graph. If True, then nodes in the resulting graph are renumbered sequentially from 0 to N-1, where N is the number of nodes. By default, the nodes are not renumbered.

Return value:

- graph
    A graph of type *GraphType* with *NIdV* nodes from the original graph.
    
    
The following example shows how to convert a subgraph between the different types of graphs::

    import snap

    V = []
    for i in range(10):
        V.append(i)

    GIn = snap.GenRndGnm(snap.TNGraph, 100, 1000)
    GOut = GIn.ConvertSubGraph(snap.TUNGraph, V)
    for NI in GOut.Nodes():
        print("node: %d" % NI.GetId())

    GIn = snap.GenRndGnm(snap.TUNGraph, 100, 1000)
    GOut = GInsnap.ConvertSubGraph(snap.TNEANet, V)
    for NI in GOut.Nodes():
        print("node: %d" % NI.GetId())

    GIn = snap.GenRndGnm(snap.TNEANet, 100, 1000)
    GOut = GInsnap.ConvertSubGraph(snap.TNGraph, V)
    for NI in GOut.Nodes():
        print("node: %d" % NI.GetId())

