GetSubGraphRenumber (SWIG)
''''''''''''''''''''''''''

.. function:: GetSubGraphRenumber(Graph, NIdV)

Returns the subgraph of *Graph* induced by the nodes in *NIdV* with renumbered node ids from 0 to N-1. This function is implemented for :class:`TNGraph` and :class:`TUNGraph`.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network.

- *NIdV*: TIntV (input)
    Node ID vector.  The subgraph consists of all nodes in *NIdV* and the edges between nodes in *NIdV*.

Return value:

- a subgraph that is the same type as *Graph* and contains the nodes from *Graph*, which have node IDs in the *NIdV* vector and all the edges with both nodes in *NIdV*. The nodes in the resulting subgraph are renumbered sequentially from 0 to N-1.

For more information, see: http://en.wikipedia.org/wiki/Glossary_of_graph_theory#Subgraphs

The following example shows how to get subgraphs for
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap
    
    Graph = snap.GenRndGnm(snap.PNGraph, 50, 500)
    Nodes = snap.TIntV()
    for N in Graph.GetNI(0).GetOutEdges():
        Nodes.Add(N)
    # Get subgraph induced by the neighbors of Node 0.
    SubGraph = snap.GetSubGraphRenumber(Graph, Nodes)
    
    Graph = snap.GenCircle(snap.PUNGraph, 100, 2, False)
    Nodes = snap.TIntV()
    for N in Graph.GetNI(50).GetOutEdges():
        Nodes.Add(N)
    SubGraph = snap.GetSubGraphRenumber(Graph, Nodes)

