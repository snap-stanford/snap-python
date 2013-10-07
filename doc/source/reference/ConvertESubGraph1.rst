ConvertESubGraph
''''''''''''''''

.. function:: ConvertESubGraph(InGraph,EIdV,RenumberNodes)

Returns a subgraph of graph *InGraph* with *EIdV* edges with an optional node renumbering.

Creates a subgraph of the input graph *InGraph* on *EIdV* edges and returns an output graph. Input and output graphs can have different types. Node and edge data is not copied, but it is shared by input and output graphs.

Parameter *RenumberNodes* determines, whether the node IDs are preserved or not. If *RenumberNodes* is false, then nodes in the resulting graph have the same node IDs as nodes in *InGraph*. If *RenumberNodes* is true, then nodes in the resulting graph are renumbered sequentially from 0 to N-1. By default, the nodes are not renumbered.

Warning: ConvertESubGraph() is only supported for TNEANet, and not for TUNGraph and TNGraph.  Edge identifiers used in *EIdV* are only available using TNEANet and not for TUNGraph and TNGraph.  TUNGraph and TNGraph Edge Ids are returned as (SrcNodeId, DstNodeId) and thus cause an error if a vector of those Graphs' edge identifiers is attempted.


Parameters:

- *InGraph*: graph (input)
    A Snap.py graph or a network 

- *EIdV*: a vector of (TNEANet) int keys (input)
    Keys are edge IDs

- *RenumberNodes*: bool (input)
    Determines if the resulting graph is renumbered or not

Return value:

- *NewGraphPt*
    A new Snap.py graph or network where node and edge data is shared by input and output graphs but are renumbered if *RenumberNodes* is true

The following code shows an example of ConvertESubGraph:

    import snap

    G1 = snap.TNEANet.New()
    G1.AddNode(1)
    G1.AddNode(2)
    G1.AddNode(3)
    G1.AddNode(4)
    G1.AddNode(5)


    G1.AddEdge(1, 2)
    G1.AddEdge(2, 3)
    G1.AddEdge(3, 4)
    G1.AddEdge(1, 3)
    G1.AddEdge(4, 5)
    G1.AddEdge(5, 4)
    G1.AddEdge(4, 1)
    G1.AddEdge(3, 1)

    FstE_Id = G1.Edges().next().GetId()

    SUBG1_edges = snap.TIntV()
    SUBG1_edges.Add(FstE_Id)
    print snap.ConvertESubGraph(G1, SUBG1_edges, True)
