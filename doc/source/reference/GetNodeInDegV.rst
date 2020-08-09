GetNodeInDegV
'''''''''''''''

.. function:: GetNodeInDegV()

A graph method that returns the in-degree for every node. 

Parameters:

- None

Return value:

- *NIdInDegV*: :class:`TIntPrV`, a vector or (int, int) pairs
	A vector of (node id, node in-degree) pairs.

The following example shows how to use :func:`GetNodeInDegV` with nodes in :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    InDegV = Graph.GetNodeInDegV()
    for item in InDegV:
        print("node ID %d: in-degree %d" % (item.GetVal1(), item.GetVal2()))

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    InDegV = UGraph.GetNodeInDegV()
    for item in InDegV:
        print("node ID %d: in-degree %d" % (item.GetVal1(), item.GetVal2()))

    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    InDegV = Network.GetNodeInDegV()
    for item in InDegV:
        print("node ID %d: in-degree %d" % (item.GetVal1(), item.GetVal2()))
