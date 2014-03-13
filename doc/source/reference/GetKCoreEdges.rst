GetKCoreEdges
'''''''''''''

.. function:: GetKCoreEdges(Graph, CoreIdSzV)

Returns the number of edges in each core of order K (where K=0, 1, ...). Stores pairs (K, number of edges) in *CoreIdSzV*.

Parameters:

- *Graph*: graph (input)
    A Snap.py graph or a network.

- *CoreIdSzV*: TIntPrV, a vector of (int, int) pairs (output)
    A vector of (order, number of edges of the given order) pairs. 

Return value:

- int
    The number of cores.


The following example shows how to get the number of edges for a given k-core in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    CoreIDSzV = snap.TIntPrV()
    kValue = snap.GetKCoreEdges(Graph, CoreIDSzV)
    for item in CoreIDSzV:
        print "order: %d edges: %d" % (item.GetVal1(), item.GetVal2())

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    CoreIDSzV = snap.TIntPrV()
    kValue = snap.GetKCoreEdges(UGraph, CoreIDSzV)
    for item in CoreIDSzV:
        print "order: %d edges: %d" % (item.GetVal1(), item.GetVal2())

    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    CoreIDSzV = snap.TIntPrV()
    kValue = snap.GetKCoreEdges(Network, CoreIDSzV)
    for item in CoreIDSzV:
        print "order: %d edges: %d" % (item.GetVal1(), item.GetVal2())
