AddSelfEdges
''''''''''''

.. function:: AddSelfEdges()

A graph method that adds a self-edge for every node in a graph.

Parameters:

- None

Return value:

- None


The following example shows how to add self edges to every node in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 10, 0)
    Graph.AddSelfEdges()
    for EI in Graph.Edges():
        print("edge: (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId()))

    UGraph = snap.GenRndGnm(snap.PUNGraph, 10, 0)
    UGraph.AddSelfEdges()
    for EI in UGraph.Edges():
        print("edge: (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId()))

    Network = snap.GenRndGnm(snap.PNEANet, 10, 0)
    Network.AddSelfEdges()
    for EI in Network.Edges():
        print("edge: (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId()))
