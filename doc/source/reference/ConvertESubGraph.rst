ConvertESubGraph
''''''''''''''''
.. note::

    This page is a draft and under revision.


.. function:: OutGraph = ConvertESubGraph(InGraph, EIdV, RenumberNodes = false)

Returns a subgraph of graph InGraph with EIdV edges with an optional node renumbering.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

- *EIdV*: a vector of ints (input)
    Edge IDs that will be included in the subgraph 

- *RenumberNodes*: boolean (input)
    Determines if nodes will be re-numbered in the subgraph

Return value:

- *OutGraph*: graph (output)
    A snap.py graph - the subgraph of InGraph

The following example shows how to create a subgraph for nodes in 
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    Some_Edges = snap.TIntV()
    Some_Edges.Add(Graph.Edges().next().GetId())
    Some_Edges.Add(Graph.Edges().next().GetId())
    Sub_Graph = ConvertESubGraph(Graph, Some_Edges, false)
    for EI in Sub_Graph.Edges():
        print "edge (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId())
    
    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    Some_Edges = snap.TIntV()
    Some_Edges.Add(Graph.Edges().next().GetId())
    Some_Edges.Add(Graph.Edges().next().GetId())
    Sub_Graph = ConvertESubGraph(Graph, Some_Edges, false)
    for EI in Sub_Graph.Edges():
        print "edge (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId())
    
    Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    Some_Edges = snap.TIntV()
    Some_Edges.Add(Graph.Edges().next().GetId())
    Some_Edges.Add(Graph.Edges().next().GetId())
    Sub_Graph = ConvertESubGraph(Graph, Some_Edges, false)
    for EI in Sub_Graph.Edges():
        print "edge (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId())
