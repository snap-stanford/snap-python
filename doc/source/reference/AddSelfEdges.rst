AddSelfEdges
''''''''''''

.. function:: AddSelfEdges(Graph)

Adds a self-edge for every node in *Graph*.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network.

Return value:

- None


The following example shows how to add self edges to every node in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 10, 0)
    snap.AddSelfEdges(Graph)
    for EI in Graph.Edges():
        print("edge: (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId()))

    UGraph = snap.GenRndGnm(snap.PUNGraph, 10, 0)
    snap.AddSelfEdges(UGraph)
    for EI in UGraph.Edges():
        print("edge: (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId()))

    Network = snap.GenRndGnm(snap.PNEANet, 10, 0)
    snap.AddSelfEdges(Network)
    for EI in Network.Edges():
        print("edge: (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId()))
