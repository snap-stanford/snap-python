ConvertESubGraph
''''''''''''''''

.. function:: ConvertESubGraph(GraphType, InGraph, EIdV, RenumberNodes=False)

Returns a subgraph of graph *InGraph* with *EIdV* edges with an optional node renumbering. The resulting subgraph will have type *GraphType*. Node and edge data is not copied, but it is shared by input and output graphs.

Parameters:

- *GraphType*: graph class (input)
    Class of output graph -- one of :class:`PNGraph`, :class:`PNEANet`, or :class:`PUNGraph`.

- *InGraph*: network (input)
    A Snap.py network.

- *EIdV*: :class:`TIntV`, a vector of ints (input)
    Edge IDs that will be included in the subgraph.

- *RenumberNodes*: bool (input)
    Determines whether the node IDs are preserved or not. If False, then nodes in the resulting graph have the same node IDs as nodes in *InGraph*. If True, then nodes in the resulting graph are renumbered sequentially from 0 to N-1, where N is the number of nodes. By default, the nodes are not renumbered.

Return value:

- graph
    A snap.py graph of type *GraphType* with *EIdV* edges from the original graph *InGraph*.


The following example shows how to create a subgraph for nodes in 
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    V = snap.TIntV()
    for i in range(100):
      V.Add(i)

    Sub_Graph = snap.ConvertESubGraph(snap.PNGraph, Network, V, False)
    for EI in Sub_Graph.Edges():
        print "edge: (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId())

    Sub_UGraph = snap.ConvertESubGraph(snap.PUNGraph, Network, V, False)
    for EI in Sub_UGraph.Edges():
        print "edge: (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId())

    Sub_Network = snap.ConvertESubGraph(snap.PNEANet, Network, V, False)
    for EI in Sub_Network.Edges():
        print "edge: (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId())