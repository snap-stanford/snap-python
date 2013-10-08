GetNodeOutDegV
''''''''''''''''
.. note::

    This page is a draft and under revision.


.. function:: GetNodeOutDegV(Graph, OutDegV)


Returns a vector of pairs for *Graph*. The node id and node out-degree are stored in *OutDeV*.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network

- *OutDegV*: a vector of pairs of integers TIntPrV (output). Keys are node IDs and out-degrees of the node.


Return value:

- None


The following example shows how to calculate GetNodeOutDegV scores for nodes in :class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

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

