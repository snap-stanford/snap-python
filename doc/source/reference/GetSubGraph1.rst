GetSubGraph
'''''''''''
.. note::

    This page is a draft and under revision.


.. function:: GetSubGraph(Graph, NIdV, RenumberNodes=False)

.. note::

    This function is not yet supported.

Returns the subgraph of *Graph* induced by the nodes in *NIdV*.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network.

- *NIdV*: TIntV (input)
    Node ID vector.  The subgraph consists of all nodes in *NIdV* and the edges between nodes in *NIdV*.

- *RenumberNodes*: boolean (input)
    Whether the node IDs are preserved or not.

Return value:

- A PGraph that is the same type as Graph.

For more information, see: http://en.wikipedia.org/wiki/Glossary_of_graph_theory#Subgraphs

The following example shows how to get subgraphs for
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap
    
    Graph = snap.GenRndGnm(snap.PNGraph, 50, 500)
    nodes = snap.TIntV()
    for N in Graph.GetNI(0).GetOutEdges():
        nodes.Add(N)
    # Get subgraph induced by the neighbors of Node 0.                                                                                                                                                        
    SubGraph = snap.GetSubGraph(Graph, nodes)
    
    Graph = snap.GenCircle(snap.PUNGraph, 100, 2, False)
    nodes = snap.TIntV()
    for N in Graph.GetNI(50).GetOutEdges():
        nodes.Add(N)
    SubGraph = snap.GetSubGraph(Graph, nodes)
    
    Graph = snap.GenFull(snap.PNEANet, 10)
    nodes = snap.TIntV()
    for i in [0, 2, 4, 6, 8]:
        nodes.Add(i)
    # Get complete subgraph induced by the even-numbered nodes.                                                                                                                                               
    SubGraph = snap.GetSubGraph(Graph, nodes)
    print SubGraph.GetEdges() # should be 20
    

