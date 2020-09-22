GetMxBiCon
'''''''''''

.. function:: GetMxBiCon()

A graph method that returns a graph representing the largest bi-connected component in the original graph. 

Parameters:

- None

Return value:

- graph
    A graph representing the largest bi-connected component in the original graph.


The following example shows how to get the largest bi-connected component in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.TNGraph, 100, 500)
    BiCon = Graph.GetMxBiCon()
    for EI in BiCon.Edges():
        print("edge: (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId()))

    UGraph = snap.GenRndGnm(snap.TUNGraph, 100, 500)
    BiCon = UGraph.GetMxBiCon()
    for EI in BiCon.Edges():
        print("edge: (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId()))

    Network = snap.GenRndGnm(snap.TNEANet, 100, 500)
    BiCon = Network.GetMxBiCon()
    for EI in BiCon.Edges():
      print("edge: (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId()))
