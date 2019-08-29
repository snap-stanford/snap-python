GetSubGraph
'''''''''''

.. function:: GetSubGraph(Graph, NIdV)

Returns an induced subgraph of an undirected graph *Graph* with *NIdV* nodes.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network.

- *NIdV*: :class:`TIntV`, a vector of ints (input)
    Vector of node ids to be included in the graph.

Return value:

- graph
    A Snap.py graph that is a subgraph of *Graph* with the nodes given by *NIdV*.


The following example shows how to return get a subgraph of
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    NIdV = snap.TIntV()
    for i in range(1, 10):
        NIdV.Add(i)

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    SubGraph = snap.GetSubGraph(Graph, NIdV)
    for EI in SubGraph.Edges():
        print("edge (%d %d)" % (EI.GetSrcNId(), EI.GetDstNId()))

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    SubGraph = snap.GetSubGraph(UGraph, NIdV)
    for EI in SubGraph.Edges():
        print("edge (%d %d)" % (EI.GetSrcNId(), EI.GetDstNId()))

    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    SubGraph = snap.GetSubGraph(Network, NIdV)
    for EI in SubGraph.Edges():
        print("edge (%d %d)" % (EI.GetSrcNId(), EI.GetDstNId()))

