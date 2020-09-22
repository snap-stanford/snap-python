GetSubGraphRenumber
'''''''''''''''''''

.. function:: GetSubGraphRenumber(NIdV)

A graph method that returns the subgraph induced by the nodes in *NIdV* with renumbered node ids from 0 to N-1. This function is implemented for :class:`TNGraph` and :class:`TUNGraph`.

Parameters:

- *NIdV*: Python list or :class:`TIntV`, a vector of ints
    Node id vector.  The subgraph consists of all nodes in *NIdV* and the edges between nodes in *NIdV*.

Return value:

- graph
    A subgraph that has the same type as the original graph and contains the nodes with ids in the *NIdV* vector and all the edges with both nodes in *NIdV*. The nodes in the resulting subgraph are renumbered sequentially from 0 to N-1.

For more information, see: http://en.wikipedia.org/wiki/Glossary_of_graph_theory#Subgraphs

The following example shows how to get subgraphs for
:class:`TNGraph` and :class:`TUNGraph`::

    import snap
    
    Graph = snap.GenRndGnm(snap.TNGraph, 50, 500)
    Nodes = []
    for N in Graph.GetNI(0).GetOutEdges():
        Nodes.append(N)
    # Get subgraph induced by the neighbors of Node 0
    SubGraph = Graph.GetSubGraphRenumber(Nodes)
    
    UGraph = snap.GenCircle(snap.TUNGraph, 100, 2, False)
    Nodes = []
    for N in UGraph.GetNI(50).GetOutEdges():
        Nodes.append(N)
    # Get subgraph induced by the neighbors of Node 50
    SubGraph = UGraph.GetSubGraphRenumber(Nodes)

