GetSubGraph
'''''''''''

.. function:: GetSubGraph(NIdV)

A graph method that returns an induced subgraph on *NIdV* nodes.

Parameters:

- *NIdV*: Python list or :class:`TIntV`, a vector of ints
    Vector of node ids to be included in the graph.

Return value:

- graph
    A graph that is a subgraph of the original graph with the nodes given by *NIdV*.


The following example shows how to return get a subgraph of
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    NIdV = []
    for i in range(1, 10):
        NIdV.append(i)

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    SubGraph = Graph.GetSubGraph(NIdV)
    for EI in SubGraph.Edges():
        print("edge (%d %d)" % (EI.GetSrcNId(), EI.GetDstNId()))

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    SubGraph = UGraph.GetSubGraph(NIdV)
    for EI in SubGraph.Edges():
        print("edge (%d %d)" % (EI.GetSrcNId(), EI.GetDstNId()))

    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    SubGraph = Network.GetSubGraph(NIdV)
    for EI in SubGraph.Edges():
        print("edge (%d %d)" % (EI.GetSrcNId(), EI.GetDstNId()))

