GetNodeOutDegV
''''''''''''''''

.. function:: GetNodeOutDegV()

A graph method that returns the out-degree for every node.

Parameters:

- None

Return value:

- *NIdOutDegV*: :class:`TIntPrV`, a vector of (int, int) pairs
    A vector of (node id, node out degree) pairs.


The following example shows how to use :func:`GetNodeOutDegV` with nodes in :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    OutDegV = Graph.GetNodeOutDegV()
    for item in OutDegV:
        print("node ID %d: out-degree %d" % (item.GetVal1(), item.GetVal2()))

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    OutDegV = UGraph.GetNodeOutDegV()
    for item in OutDegV:
        print("node ID %d: out-degree %d" % (item.GetVal1(), item.GetVal2()))

    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    OutDegV = Network.GetNodeOutDegV()
    for item in OutDegV:
        print("node ID %d: out-degree %d" % (item.GetVal1(), item.GetVal2()))

