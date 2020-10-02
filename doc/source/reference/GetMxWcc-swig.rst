GetMxWcc (SWIG)
''''''''''''''''''

.. function:: GetMxWcc(Graph)
   :noindex:

Returns a graph representing the largest weakly connected component in *Graph*.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

Return value:

- graph
	A Snap.py graph or a network representing the largest weakly connected component in *Graph*.


The following example shows how to get the largest weakly connected component in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 500)
    MxWcc = snap.GetMxWcc(Graph)
    for EI in MxWcc.Edges():
        print("edge: (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId()))

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 500)
    MxWcc = snap.GetMxWcc(UGraph)
    for EI in MxWcc.Edges():
        print("edge: (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId()))

    Network = snap.GenRndGnm(snap.PNEANet, 100, 500)
    MxWcc = snap.GetMxWcc(Network)
    for EI in MxWcc.Edges():
        print("edge: (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId()))
