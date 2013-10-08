ConvertSubGraph 
'''''''''''''''

.. function:: OutGraph ConvertSubGraph (GraphType, InGraph, NIdV, RenumberNodes = False)

Returns an induced subgraph of graph InGraph with NIdV nodes with an optional node renumbering.

Creates a subgraph of the input graph InGraph on NIdV nodes and returns an output graph. Input and output graphs can have different types, where the output graph type is specified by GraphType. Node and edge data is not copied, but it is shared by input and output graphs.

Parameter RenumberNodes determines, whether the node IDs are preserved or not. If RenumberNodes is False, then nodes in the resulting graph have the same node IDs as nodes in InGraph. If RenumberNodes is True, then nodes in the resulting graph are renumbered sequentially from 0 to N-1. By default, the nodes are not renumbered.

Parameters:

- *GraphType*: graph type (input)
    One of: PNGraph (directed graph), PUNGraph (undirected graph), PNEANet (directed network)

- *InGraph*: graph (input)
    A Snap.py graph or a network

- *NIdV*: a vector of int values (input)
    Node IDs to be included in the returned subgraph

- *RenumberNodes*: boolean (input)
    Determines whether the node IDs are preserved or not

Return value:

- *OutGraph*: graph
    A Snap.py graph or a network, which is the vertex-induced subgraph

For more info see: http://mathworld.wolfram.com/Vertex-InducedSubgraph.html

The following example shows how to get the vertex-induced subgraph and have that subgraph be either a :class:`TNGraph`, :class:`TUNGraph`, or :class:`TNEANet`::

    import snap

    v = snap.TIntV()
    v.Add(1)
    v.Add(2)
    
    G1 = snap.GenRndGnm(snap.PNGraph, 5, 10)
    G2 = snap.GenRndGnm(snap.PUNGraph, 5, 10)
    G3 = snap.GenRndGnm(snap.PNEANet, 5, 10)
    
    N1 = snap.ConvertSubGraph(snap.PNGraph, G1, v)
    N2 = snap.ConvertSubGraph(snap.PUNGraph, G2, v, False)
    N3 = snap.ConvertSubGraph(snap.PNEANet, G3, v, True)

    print "Number of Nodes:", N1.GetNodes()
    print "Number of Nodes:", N2.GetNodes()
    print "Number of Nodes:", N3.GetNodes()
