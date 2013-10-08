ConvertESubGraph
''''''''''''''''

.. function:: ConvertESubGraph(OutGraphType, InGraph, EIdV, RenumberNodes=False)

Returns a subgraph of graph InGraph containing the edges in EIdV, with an optional node renumbering. Node and edge data is not copied, but it is shared by input and output graphs.

Parameters:

- *OutGraphType*: Snap graph type (input)
    A Snap.py graph type, e.g. snap.PUNGraph

- *InGraph*: network (input)
    A Snap.py network, i.e. of type snap.TNEANet.

- *EIdV*: TIntV (input)
    TIntV containing the edges to be contained in the returned subgraph.

- *RenumberNodes*: bool (input)
    True if the node IDs should be renumbered. If RenumberNodes is false, nodes in the returned graph have the same node IDs as in the input graph. If RenumberNodes is true, nodes in the returned graph are renumbered sequentially from 0 to N-1, where N is the number of nodes in the returned subgraph. By default, the nodes are not renumbered. 

Return value:

- Graph of type OutGraphType, which is constructed as the subgraph of *InGraph* containing the edges in EIdV and the nodes adjacent to at least one edge from EIdV. 

An example::

    import snap

    G = snap.TNEANet.New()
    G.AddNode(1)
    G.AddNode(2)
    G.AddNode(3)
    G.AddEdge(1, 2, 11)
    G.AddEdge(1, 3, 22)

    EIdV = snap.TIntV()
    EIdV.Add(11)
    SubGraph = snap.ConvertESubGraph(snap.PUNGraph, G, EIdV, False)
