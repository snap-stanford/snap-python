DelDegKNodes
''''''''''''

.. function:: DelDegKNodes(OutDegK, InDegK)

A graph method that removes all nodes of out-degree *OutDegK* and all nodes of in-degree *InDegK* from a graph.

Parameters:

- *OutDegK*: int
    Specifies out-degree of nodes to be removed.

- *InDegK*: int
	Specifies in-degree of nodes to be removed.
	
Return value:

- None


The following example shows how to remove nodes with out-degree *OutDegK* or in-degree *InDegK* in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.TNGraph, 100, 10)
    Graph.DelDegKNodes(1, 1)
    for NI in Graph.Nodes():
        if NI.GetOutDeg() == 1:
            print("Node %d has out-degree 1." % NI.GetId())
        if NI.GetInDeg() == 1:
            print("Node %d has in-degree 1." % NI.GetId())
    
    UGraph = snap.GenRndGnm(snap.TUNGraph, 100, 10)
    UGraph.DelDegKNodes(1, 1)
    for NI in UGraph.Nodes():
        if NI.GetOutDeg() == 1:
            print("Node %d has out-degree 1." % NI.GetId())
        if NI.GetInDeg() == 1:
            print("Node %d has in-degree 1." % NI.GetId())

    Network = snap.GenRndGnm(snap.TNEANet, 100, 10)
    Network.DelDegKNodes(1, 1)
    for NI in Network.Nodes():
        if NI.GetOutDeg() == 1:
            print("Node %d has out-degree 1." % NI.GetId())
        if NI.GetInDeg() == 1:
            print("Node %d has in-degree 1." % NI.GetId())
