GetNodeOutDegV
''''''''''''''''

.. function:: GetNodeOutDegV(Graph, NIdOutDegV)

Computes the out-degree for every node in *Graph*. 
The result is stored in *NIdOutDegV*, a vector of pairs (node id, node out degree).

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network.

- *NIdOutDegV*: TIntPrV, a vector of (int, int) pairs (output)
    A vector of (node id, node out degree) pairs.

Return value:

- None


The following example shows how to use :func:`GetNodeOutDegV` with nodes in :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    OutDegV = snap.TIntPrV()
    snap.GetNodeOutDegV(Graph, OutDegV)
    for item in OutDegV:
        print "node ID %d: out-degree %d" % (item.GetVal1(), item.GetVal2())

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    OutDegV = snap.TIntPrV()
    snap.GetNodeOutDegV(UGraph, OutDegV)
    for item in OutDegV:
        print "node ID %d: out-degree %d" % (item.GetVal1(), item.GetVal2())

    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    OutDegV = snap.TIntPrV()
    snap.GetNodeOutDegV(Network, OutDegV)
    for item in OutDegV:
        print "node ID %d: out-degree %d" % (item.GetVal1(), item.GetVal2())

