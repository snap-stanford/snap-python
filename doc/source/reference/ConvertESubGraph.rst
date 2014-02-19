ConvertESubGraph
''''''''''''''''

.. function:: ConvertESubGraph(GraphType, InGraph, EIdV, RenumberNodes=False)

Returns a subgraph of graph *InGraph* with *EIdV* edges with an optional node renumbering. The returned subgraph will have type *GraphType*.

Parameters:

- *GraphType*: graph class (input)
    Class of output graph -- one of `PNGraph`, `PNEANet`, or `PUNGraph`

- *InGraph*: network (input)
    A Snap.py network

- *EIdV*: TIntV, a vector of ints (input)
    Edge IDs that will be included in the subgraph 

- *RenumberNodes*: boolean (input)
    Determines if nodes will be re-numbered in the subgraph

Return value:

- graph
    A snap.py graph of type *GraphType* with *EIdV* edges from the original graph *InGraph*

The following example shows how to create a subgraph for nodes in 
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    V = snap.TIntV()
    for i in range(100):
      V.Add(i)

    Sub_Graph = snap.ConvertESubGraph(snap.PNGraph, Graph, V, False)
    for EI in Sub_Graph.Edges():
        print "edge (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId())

    Sub_Graph = snap.ConvertESubGraph(snap.PUNGraph, Graph, V, False)
    for EI in Sub_Graph.Edges():
        print "edge (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId())
