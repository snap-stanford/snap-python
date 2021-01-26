GetGraphUnion
'''''''''''''

.. function:: GetGraphUnion(Graph)

A graph method that computes a graph union between two graphs, the graph object and the *Graph* parameter. The graph object and the *Graph* parameter must be of the same type. The graph union is computed by adding to the graph object nodes and edges from *Graph* that are not already in the graph object. The resulting graph union is stored in the graph object and also returned as a result. 

The graph union for type :class:`TNEANet` has some specific properties in dealing with multi edges and edge IDs. In the case of multiple edges between two nodes, only one edge will be added between two nodes and only when that edge does not yet exist in the graph object. This means that the union will preserve any multi edges in the graph object, but will not create new multi edges. Edges are directed, so edges with swapped source and destination nodes are treated as separate. Edge IDs from *Graph* are not preserved in the graph union.

Parameters:

- *Graph*: graph object
    An object instance of type TNGraph, TUNGraph or TNEANet, must be the same type as the graph object.

Return value:

- graph
    The resulting union graph, the same as the graph object.

The following example shows how to compute a union with graphs of type :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    G1 = snap.GenRndGnm(snap.TNGraph, 100, 1000)
    G2 = snap.GenRndGnm(snap.TNGraph, 100, 1000)
    G1.GetGraphUnion(G2)

    G3 = snap.GenRndGnm(snap.TUNGraph, 100, 1000)
    G4 = snap.GenRndGnm(snap.TUNGraph, 100, 1000)
    G3.GetGraphUnion(G4)

    G5 = snap.GenRndGnm(snap.TNEANet, 100, 1000)
    G6 = snap.GenRndGnm(snap.TNEANet, 100, 1000)
    G5.GetGraphUnion(G6)

