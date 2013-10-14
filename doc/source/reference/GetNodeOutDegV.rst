GetNodeOutDegV
''''''''''''''''

.. function:: GetNodeOutDegV(Graph, NIdOutDegV)

Computes the out-degree for every node in *Graph*. 
The result is stored in *NIdOutDegV*, a vector of pairs (node id, node out degree).

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

- *NIdOutDegV*: TIntPrV, a vector of (int, int) pairs (output)
    A vecotr of (node id, node out degree) pairs.

Return value:

- None


The following example shows how to use :func:`GetNodeOutDegV` with nodes in :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    OutDegV = snap.TIntPrV()
    snap.GetNodeOutDegV(Graph, OutDegV)
    for p in OutDegV:
        print "node ID %d: degree %d" % (p.GetVal1(), p.GetVal2())

    Graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    OutDegV = snap.TIntPrV()
    snap.GetNodeOutDegV(Graph, OutDegV)
    for p in OutDegV:
        print "node ID %d: degree %d" % (p.GetVal1(), p.GetVal2())

    Graph = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    OutDegV = snap.TIntPrV()
    snap.GetNodeOutDegV(Graph, OutDegV)
    for p in OutDegV:
        print "node ID %d: degree %d" % (p.GetVal1(), p.GetVal2())

