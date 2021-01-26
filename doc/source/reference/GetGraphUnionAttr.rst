GetGraphUnionAttr
'''''''''''''''''

.. function:: GetGraphUnionAttr(Graph)

A graph method that computes a graph union with attributes between two graphs, the graph object and the *Graph* parameter. The graph object and the *Graph* parameter must be of type :class:`TNEANet`. The graph union with attributes is computed by adding to the graph object nodes and edges from *Graph* that are not already in the graph object. The corresponding attributes are copied as well. The resulting graph union is stored in the graph object and also returned as a result. 

The graph union has some specific properties in dealing with multi edges and edge IDs. In the case of multiple edges between two nodes, only one edge will be added between two nodes and only when that edge does not yet exist in the graph object. This means that the union will preserve any multi edges in the graph object, but will not create new multi edges. Edges are directed, so edges with swapped source and destination nodes are treated as separate. Edge IDs from *Graph* are not preserved in the graph union.

Parameters:

- *Graph*: graph object
    An object instance of type TNEANet.

Return value:

- graph
    The resulting union graph, the same as the graph object.

The following example shows how to compute a graph union with attributes for :class:`TNEANet`::

    import snap

    G1 = snap.GenRndGnm(snap.TNEANet, 100, 1000)
    s = "attr"
    count = 0
    for NI in G1.Nodes():
        count += 1
        G1.AddIntAttrDatN(NI.GetId(), count, s)
    count = 0
    for EI in G1.Edges():
        count += 1
        G1.AddIntAttrDatE(EI.GetId(), count, s)

    G2 = snap.GenRndGnm(snap.TNEANet, 100, 1000)
    count = 0
    for NI in G2.Nodes():
        count += 1
        G2.AddIntAttrDatN(NI.GetId(), count, s)
    count = 0
    for EI in G2.Edges():
        count += 1
        G2.AddIntAttrDatE(EI.GetId(), count, s)

    G1.GetGraphUnionAttr(G2)

