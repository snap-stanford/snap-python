ConvertESubGraph
''''''''''''''''

.. function:: ConvertESubGraph(GraphType, EIdV, RenumberNodes=False)

A graph method that returns a subgraph of the original graph with *EIdV* edges with an optional node renumbering. The resulting subgraph will have type *GraphType*. Any node and edge data is not copied, but it is shared by input and output graphs.

Parameters:

- *GraphType*: graph class
    Class of output graph -- one of TNGraph, TUNGraph or TNEANet.

- *EIdV*: Python list or :class:`TIntV`, a vector of ints
    Edge ids that will be included in the subgraph.

- (optional) *RenumberNodes*: bool
    Determines whether the node ids are preserved or not. If False, then nodes in the resulting graph have the same node ids as nodes in the original graph. If True, then nodes in the resulting graph are renumbered sequentially from 0 to N-1, where N is the number of nodes. By default, the nodes are not renumbered.

Return value:

- graph
    A graph of type *GraphType* with *EIdV* edges from the original graph.


The following example shows how to create a subgraph for nodes in 
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Network = snap.GenRndGnm(snap.TNEANet, 100, 1000)
    V = []
    for i in range(100):
      V.append(i)

    Sub_Graph = Network.ConvertESubGraph(snap.TNGraph, V)
    for EI in Sub_Graph.Edges():
        print("edge: (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId()))

    Sub_UGraph = Network.ConvertESubGraph(snap.TUNGraph, V)
    for EI in Sub_UGraph.Edges():
        print("edge: (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId()))

    Sub_Network = Network.ConvertESubGraph(snap.TNEANet, V)
    for EI in Sub_Network.Edges():
        print("edge: (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId()))
