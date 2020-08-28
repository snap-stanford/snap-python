GetKCoreEdges
'''''''''''''

.. function:: GetKCoreEdges()

Returns the number of edges in each core of order K (where K=0, 1, ...).

Parameters:

- None

Return value:

- int
    The number of cores.

- :class:`TIntPrV`, a vector of (int, int) pairs (output)
    A vector of (order K, number of edges of the given order) pairs. 

The following example shows how to get the number of edges for a given k-core in
:class:`TNGraph`, :class:`TUNGraph`, and :class:`TNEANet`::

    import snap

    Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
    kValue, CoreIDSzV = Graph.GetKCoreEdges()
    for item in CoreIDSzV:
        print("order: %d edges: %d" % (item.GetVal1(), item.GetVal2()))

    UGraph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    kValue, CoreIDSzV = UGraph.GetKCoreEdges()
    for item in CoreIDSzV:
        print("order: %d edges: %d" % (item.GetVal1(), item.GetVal2()))

    Network = snap.GenRndGnm(snap.PNEANet, 100, 1000)
    kValue, CoreIDSzV = Network.GetKCoreEdges()
    for item in CoreIDSzV:
        print("order: %d edges: %d" % (item.GetVal1(), item.GetVal2()))
