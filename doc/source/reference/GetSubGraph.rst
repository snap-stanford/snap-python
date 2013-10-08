GetSubGraph
'''''''''''
.. note::

    This page is a draft and under revision.


.. function:: GetSubGraph(Graph, NIdV, RenumberNodes=false)

Returns an induced subgraph of an undirected graph *Graph* with *NIdV* nodes with an optional node renumbering.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

- *NIdV*: a vector of int keys (input)
    Graph nodes. Keys are node IDs.

- *RenumberNodes*: boolean (input)
    Whether the node IDs are preserved or not.

Return value:

- SubGraph

The following example shows how to return GetSubGraph for nodes in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    NIdV = snap.TIntV()
    for i in range(1, 10 + 1):
        NIdV.Add(i)
    SubGraph = snap.GetSubGraph(Graph, NIdV)
    for edge in SubGraph.Edges():
        print "edge (%d %d)" % (edge.GetSrcNId(), edge.GetDstNId())

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    NIdV = snap.TIntV()
    for i in range(1, 10 + 1):
        NIdV.Add(i)
    SubGraph = snap.GetSubGraph(Graph, NIdV)
    for edge in SubGraph.Edges():
        print "edge (%d %d)" % (edge.GetSrcNId(), edge.GetDstNId())

    Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    NIdV = snap.TIntV()
    for i in range(1, 10 + 1):
        NIdV.Add(i)
    SubGraph = snap.GetSubGraph(Graph, NIdV)
    for edge in SubGraph.Edges():
        print "edge (%d %d)" % (edge.GetSrcNId(), edge.GetDstNId())

