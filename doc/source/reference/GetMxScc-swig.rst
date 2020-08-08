GetMxScc (SWIG)
'''''''''''''''

.. function:: GetMxScc(Graph)

Returns a graph representing the largest strongly connected component in *Graph*.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network.

Return value:

- graph
    A Snap.py graph or a network representing the largest strongly connected component in *Graph*.


The following example shows how to get the largest strongly connected component in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 500)
    MxScc = snap.GetMxScc(Graph)
    for EI in MxScc.Edges():
        print("edge: (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId()))

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 500)
    MxScc = snap.GetMxScc(UGraph)
    for EI in MxScc.Edges():
        print("edge: (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId()))

    Network = snap.GenRndGnm(snap.PNEANet, 100, 500)
    MxScc = snap.GetMxScc(Network)
    for EI in MxScc.Edges():
        print("edge: (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId()))
