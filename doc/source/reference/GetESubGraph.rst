GetESubGraph
''''''''''''

.. function:: GetESubGraph(Graph, EIdV)

Returns a subgraph of graph *Graph* with *EIdV* edges.

The resulting subgraph contains all the edges from *Graph*, which have edge IDs in the *EIdV* vector and all the nodes which connect to at least one edge in *EIdV*. Node and edge IDs are preserved. Nodes and edges in the resulting subgraph have the same IDs as in *Graph*.

Use this function for multi-graphs, where the edges have edge IDs (class TNEANet).

Parameters:

- *Graph*: graph (input)
    A Snap.py network.

- *EIdV*: vector (input)
    A vector of edge IDs in graph.

Return value:

- A subgraph of graph *Graph* with *EIdV* edges.

Since this function will only work with graphs where the edges have unique identifiers, it cannot be called on objects of class TUNGraph and TNGraph.

The following example shows how to use GetESubGraph for
:class:`TNEANet`::

    import snap

    # The following function includes every edge in the original
    # graph, so the subgraph should equal the original graph.

    Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    EIdV = snap.TIntV()
    for edge in Graph.Edges():
        EIdV.Add(edge.GetId())
    ESubGraph = snap.GetESubGraph(Graph, EIdV)
