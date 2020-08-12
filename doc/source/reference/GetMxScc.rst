GetMxScc
''''''''

.. function:: GetMxScc()

A graph method that returns a graph representing the largest strongly connected component in the original graph.

Parameters:

- None

Return value:

- graph
    A graph representing the largest strongly connected component in the original graph.


The following example shows how to get the largest strongly connected component in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 500)
    MxScc = Graph.GetMxScc()
    for EI in MxScc.Edges():
        print("edge: (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId()))

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 500)
    MxScc = UGraph.GetMxScc()
    for EI in MxScc.Edges():
        print("edge: (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId()))

    Network = snap.GenRndGnm(snap.PNEANet, 100, 500)
    MxScc = Network.GetMxScc()
    for EI in MxScc.Edges():
        print("edge: (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId()))
