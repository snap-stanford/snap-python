GetMxBiCon
'''''''''''

.. function:: GetMxBiCon(Graph)

Returns a graph representing the largest bi-connected component in *Graph*. 

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network.

Return value:

- graph
    A Snap.py graph or a network representing the largest bi-connected component in *Graph*.


The following example shows how to get the largest bi-connected component in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 500)
    BiCon = snap.GetMxBiCon(Graph)
    for EI in BiCon.Edges():
        print "edge: (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId())

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 500)
    BiCon = snap.GetMxBiCon(UGraph)
    for EI in BiCon.Edges():
        print "edge: (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId())

    Network = snap.GenRndGnm(snap.PNEANet, 100, 500)
    BiCon = snap.GetMxBiCon(Network)
    for EI in BiCon.Edges():
      print "edge: (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId())
