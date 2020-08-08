DelDegKNodes (SWIG)
'''''''''''''''''''

.. function:: DelDegKNodes(Graph, OutDegK, InDegK)

Removes all nodes of out-degree *OutDegK* and all nodes of in-degree *InDegK* from *Graph*. 

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network.

- *OutDegK*: int (input)
    Specifies out-degree of nodes to be removed.

- *InDegK*: int (input)
	Specifies in-degree of nodes to be removed.
	
Return value:

- None


The following example shows how to remove nodes with out-degree *OutDegK* or in-degree *InDegK* in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 10)
    snap.DelDegKNodes(Graph, 1, 1)
    for NI in Graph.Nodes():
        if NI.GetOutDeg() == 1:
            print("Node %d has out-degree 1." % NI.GetId())
        if NI.GetInDeg() == 1:
            print("Node %d has in-degree 1." % NI.GetId())
    
    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 10)
    snap.DelDegKNodes(UGraph, 1, 1)
    for NI in UGraph.Nodes():
        if NI.GetOutDeg() == 1:
            print("Node %d has out-degree 1." % NI.GetId())
        if NI.GetInDeg() == 1:
            print("Node %d has in-degree 1." % NI.GetId())

    Network = snap.GenRndGnm(snap.PNEANet, 100, 10)
    snap.DelDegKNodes(Network, 1, 1)
    for NI in Network.Nodes():
        if NI.GetOutDeg() == 1:
            print("Node %d has out-degree 1." % NI.GetId())
        if NI.GetInDeg() == 1:
            print("Node %d has in-degree 1." % NI.GetId())
